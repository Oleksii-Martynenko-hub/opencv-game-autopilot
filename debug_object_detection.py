import cv2 as cv
import numpy as np
import pyautogui as pg
from mss import mss, tools
from pynput.keyboard import Key, KeyCode, Listener as KeyListener
from pynput.mouse import Button, Controller, Listener as MouseListener

from window_capture import WindowCapture
from vision import Vision
from filters.hsvfilter import HsvFilter


def shot(name, position=None, times=1):
    top, left, width, height = position
    sct = mss()
    path = "images/" + name + ".jpeg"
    for i in range(times):
        img = sct.grab({"top": top, "left": left, "width": width, "height": height})
        tools.to_png(img.rgb, img.size,  output=path)


screenshot_position = [0, 0, 0, 0]


def take_screenshot(name, position=None, times=1):
    if position:
        pg.countdown(5)
        shot(name, position, times)
    else:
        hold_list = []

        def add_to_hold_list(key):
            hold_list.append(key)

        def set_left_top(x, y):
            global screenshot_position

            screenshot_position[0] = y
            screenshot_position[1] = x

        def set_width_height(x, y):
            global screenshot_position

            screenshot_position[2] = x - screenshot_position[1]
            screenshot_position[3] = y - screenshot_position[0]

        def on_release(key):
            if key == Key.cmd and Key.shift in hold_list:
                set_left_top(*pg.position())

            if key == Key.alt and Key.shift in hold_list:
                set_width_height(*pg.position())

            hold_list.remove(key)

            if key == Key.esc:
                print(screenshot_position)
                shot(name, screenshot_position, times)
                return False

        with KeyListener(on_press=add_to_hold_list, on_release=on_release) as listener:
            listener.join()


class DebugObjectDetection:
    template: np.ndarray = None
    hsv_filter: HsvFilter = None
    window: WindowCapture = None
    vision: Vision = None
    cropped_region = None

    def __init__(self, template: np.ndarray, threshold=None, hsv_filter: HsvFilter = None):
        self.template = template
        self.hsv_filter = hsv_filter
        self.threshold = threshold

        print("Finding window...")
        self.window = WindowCapture()

    def set_cropped_region(self, crop_top: int = 0, crop_right: int = 0, crop_bottom: int = 0, crop_left: int = 0):
        top, left, width, height = self.window.getRegion().values()

        self.cropped_region = {"top": top + crop_top, "left": left + crop_left,
                               "width": width - crop_left - crop_right, "height": height - crop_top - crop_bottom}

    def start(self, debug_mode: "origin" or "processed" or "threshold" = "origin",
              draw_mode: "rectangles" or "points" or "both" = "points", is_show_template: bool = False, scale=100):

        print("Creating vision...")
        self.vision = Vision(self.template, hsv_filter=self.hsv_filter)

        if debug_mode == "processed":
            print("Initializing trackbars GUI...")
            self.vision.init_control_gui()

        if debug_mode == "threshold":
            print("Initializing trackbars GUI...")
            self.vision.init_threshold_control_gui()

        region = None
        if self.cropped_region is not None:
            print("Setting cropped region...")
            region = self.cropped_region

        # processed = self.vision.apply_hsv_filter(origin, hsv_filter=self.hsv_filter)
        cv.imshow("DebugObjectDetection template original", self.vision.template_original)

        print("Starting looping...")
        # scale_percent = 100  # percent of original size
        while True:
            if is_show_template and self.vision.template_processed is not None:
                cv.imshow("DebugObjectDetection template processed", self.vision.template_processed)

            origin = self.window.getScreenshot(region)

            processed = self.vision.apply_hsv_filter(origin, hsv_filter=self.hsv_filter)

            width = int(origin.shape[1] * scale / 100)
            height = int(origin.shape[0] * scale / 100)
            dim = (width, height)
            #
            # original_img = self.vision.template_original
            # self.vision.template_original = cv.resize(original_img, dim)
            rectangles = self.vision.find(processed, threshold=self.threshold, debug=debug_mode == "threshold" or debug_mode == "processed")
            # self.vision.template_original = original_img
            #
            # if len(rectangles) == 0:
            #     if scale_percent < 81:
            #         scale_percent = 121
            #     scale_percent -= 1

            self.window.getAverageFps()

            if debug_mode == "origin" or debug_mode == "threshold":
                output = self.draw(origin, rectangles, draw_mode)
                output = cv.resize(output, dim, interpolation=cv.INTER_AREA)
                cv.imshow("DebugObjectDetection haystack", output)
            else:
                output = self.draw(processed, rectangles, draw_mode)
                output = cv.resize(output, dim, interpolation=cv.INTER_AREA)
                cv.imshow("DebugObjectDetection haystack", output)

            key = cv.waitKey(1)
            if key == 27:
                break

        print('HsvFilter: ', end='')
        print(f" \
            hMin={self.vision.get_hsv_filter_from_controls().hMin},\
            sMin={self.vision.get_hsv_filter_from_controls().sMin},\
            vMin={self.vision.get_hsv_filter_from_controls().vMin},\
            hMax={self.vision.get_hsv_filter_from_controls().hMax},\
            sMax={self.vision.get_hsv_filter_from_controls().sMax},\
            vMax={self.vision.get_hsv_filter_from_controls().vMax},\
            sAdd={self.vision.get_hsv_filter_from_controls().sAdd},\
            sSub={self.vision.get_hsv_filter_from_controls().sSub},\
            vAdd={self.vision.get_hsv_filter_from_controls().vAdd},\
            vSub={self.vision.get_hsv_filter_from_controls().vSub},\
        ")
        print('EdgeFilter: ', end='')
        print([
            self.vision.get_edge_filter_from_controls().kernelSize,
            self.vision.get_edge_filter_from_controls().erodeIter,
            self.vision.get_edge_filter_from_controls().dilateIter,
            self.vision.get_edge_filter_from_controls().canny1,
            self.vision.get_edge_filter_from_controls().canny2,
        ])
        print(f'Threshold: {self.vision.threshold}')

        stop_watching = self.window.startWatchdogOnActive()

        stop_watching()

        cv.destroyAllWindows()

    def draw(self, img, rectangles, draw_mode: "rectangles" or "points" or "both" = "points"):
        if draw_mode == "rectangles":
            return self.vision.draw_rectangles(img, rectangles)

        if draw_mode == "points":
            points = self.vision.get_click_points(rectangles)
            return self.vision.draw_crosshairs(img, points)

        if draw_mode == "both":
            output = self.vision.draw_rectangles(img, rectangles)
            points = self.vision.get_click_points(rectangles)
            return self.vision.draw_crosshairs(output, points)


if __name__ == "__main__":
    temp = cv.imread(
        'images/bridgewatch_faction_sign.jpeg', cv.IMREAD_UNCHANGED)

    # cv.imshow('original template outside', temp)

    # TODO: check hsv filter origin/template, looks different
    hsv_filter = HsvFilter.player_hp_bar()

    # rgb = cv.cvtColor(temp, cv.COLOR_BGR2RGB)
    # bgr = cv.cvtColor(rgb, cv.COLOR_RGB2BGR)

    dod = DebugObjectDetection(temp, threshold=0.95,  hsv_filter=HsvFilter(hMin=0, sMin=0, vMin=0, hMax=179, sMax=255, vMax=255, sAdd=0, sSub=0, vAdd=0, vSub=0))
    # t, l, w, h = 90, 90, 240, 130
    t, l, w, h = 850, 370, 115, 110
    or_w = dod.window.getRegion()['width']
    or_h = dod.window.getRegion()['height']
    dod.set_cropped_region(crop_top=t, crop_left=l, crop_right=or_w-l-w, crop_bottom=or_h-t-h)

    dod.start("origin", "points", is_show_template=True, scale=350)

    # take_screenshot('lymhurst_market', [86, 1262, 279, 35])

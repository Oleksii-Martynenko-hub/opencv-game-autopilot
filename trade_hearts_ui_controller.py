import cv2 as cv
import pyautogui as pg

from filters.hsvfilter import HsvFilter
from vision import Vision
from window_capture import WindowCapture
from custom_math import CustomMath as cmath


class TradeHeartsUIController:
    screenW = pg.size()[0]
    screenH = pg.size()[1]
    screen_region = dict(top=0, left=0, width=screenW, height=screenH)

    def __init__(self, window: WindowCapture, city="bridgewatch"):
        self.window = window
        self.city = city

    def get_screen_point(self, point, find_region):
        win_top = self.window.getRegion()['top']
        win_left = self.window.getRegion()['left']
        t, l, w, h = find_region.values()
        region = {'top': win_top + t, 'left': win_left + l, 'width': w, 'height': h}

        rel_pt = cmath.get_relative_point(self.window.getRegion(), region, child_point=point)
        return cmath.get_relative_point(self.screen_region, self.window.getRegion(), child_point=rel_pt)

    def find_element(self, element, not_success_callback, find_region: dict, should_find=True, threshold=0.95, hsv_filter=None):
        is_first = True
        vision = Vision(cv.imread(element, cv.IMREAD_UNCHANGED), hsv_filter=hsv_filter)

        win_top = self.window.getRegion()['top']
        win_left = self.window.getRegion()['left']
        t, l, w, h = find_region.values()
        region = {'top': win_top + t, 'left': win_left + l, 'width': w, 'height': h}

        while True:
            frame = self.window.getScreenshot(region)
            if hsv_filter is None:
                frame = vision.apply_hsv_filter(frame, hsv_filter=HsvFilter(hMin=0, sMin=0, vMin=0, hMax=179, sMax=255, vMax=255, sAdd=0, sSub=0, vAdd=0, vSub=0))
            if hsv_filter is not None:
                frame = vision.apply_hsv_filter(frame, hsv_filter=hsv_filter)

            rectangles = vision.find(frame, threshold=threshold)
            points = vision.get_click_points(rectangles)

            if should_find:
                if len(points) > 0:
                    print(' +')
                    return points

                if len(points) <= 0:
                    not_success_callback(is_first)
                    if is_first:
                        is_first = False

            if not should_find:
                if len(points) <= 0:
                    print(' +')

                if len(points) > 0:
                    not_success_callback(is_first)
                    if is_first:
                        is_first = False

    def open_trade_mission_window(self):
        def click_at_vendor(is_first):
            if is_first:
                print("Opening trade mission window...")
            else:
                print("Can't open trade mission window")
            pg.click()
            pg.sleep(0.15)

        find_region = {'top': 475, 'left': 475, 'width': 80, 'height': 100}

        points = self.find_element(
            'images/trade_mission_tab.jpeg',
            click_at_vendor,
            find_region,
        )

        pg.moveTo(*self.get_screen_point(points[0], find_region), duration=0.15)

    def open_trade_mission_tab(self):
        def click_at_tab(is_first):
            if is_first:
                print("Opening trade mission tab...")
            else:
                print("Can't open trade mission tab")
            pg.click()
            pg.sleep(0.15)

        find_region = {'top': 380, 'left': 37, 'width': 270, 'height': 50}

        points = self.find_element(
            'images/trade_mission_lymhurst.jpeg',
            click_at_tab,
            find_region,
        )

        pg.moveTo(*self.get_screen_point(points[0], find_region), duration=0.15)

    def open_lymhurst_mission(self):
        def click_at_lymhurst(is_first):
            if is_first:
                print("Opening major mission...")
            else:
                print("Can't open major mission")
            pg.click()
            pg.sleep(0.25)

        find_region = {'top': 620, 'left': 100, 'width': 350, 'height': 150}

        points = self.find_element(
            'images/major_trade_mission_treeheart.jpeg',
            click_at_lymhurst,
            find_region,
        )

        pg.moveTo(*self.get_screen_point(points[0], find_region), duration=0.15)

    def open_major_mission_dialog(self):
        def click_at_major_mission(is_first):
            if is_first:
                print("Opening major mission dialog...")
            else:
                print("Can't open major mission dialog")
            pg.click()
            pg.sleep(0.35)

        find_region = {'top': 140, 'left': 850, 'width': 310, 'height': 130}

        points = self.find_element(
            'images/major_contract_treeheart_dialog.jpeg',
            click_at_major_mission,
            find_region,
        )

        pg.moveTo(*self.get_screen_point(points[0], find_region), duration=0.15)

    def click_contract_accept_btn(self):
        def click_at_accept_btn(is_first):
            if is_first:
                print("Finding accept btn...")
            else:
                print("Can't find accept btn")

        find_region = {'top': 840, 'left': 1000, 'width': 225, 'height': 100}

        points = self.find_element(
            'images/major_contract_accept_btn.jpeg',
            click_at_accept_btn,
            find_region,
        )

        pg.click(*self.get_screen_point(points[0], find_region), duration=0.15)
        pg.move(0, 40, duration=0.15)
        pg.sleep(0.2)

        def click_at_accept_btn(is_first):
            if is_first:
                print("Finding accept btn...")
            else:
                print("Still found accept btn")
                pg.move(0, -40, duration=0.15)
                pg.click()
                pg.move(0, 40, duration=0.15)
                pg.sleep(0.25)

        find_region = {'top': 840, 'left': 1000, 'width': 225, 'height': 100}

        self.find_element(
            'images/major_contract_accept_btn.jpeg',
            click_at_accept_btn,
            find_region,
            should_find=False
        )

    def click_contract_give_items_btn(self):
        def click_at_accept_btn(is_first):
            if is_first:
                print("Finding give items btn...")
            else:
                print("Can't find give items btn")

        find_region = {'top': 840, 'left': 1000, 'width': 225, 'height': 100}

        points = self.find_element(
            'images/trade_mission_give_items_btn.jpeg',
            click_at_accept_btn,
            find_region,
        )

        pg.click(*self.get_screen_point(points[0], find_region), duration=0.15)
        pg.move(0, 40, duration=0.15)
        pg.sleep(0.2)

        def click_at_accept_btn(is_first):
            if is_first:
                print("Finding give items btn...")
            else:
                print("Still found give items btn")
                pg.move(0, -40, duration=0.15)
                pg.click()
                pg.move(0, 40, duration=0.15)
                pg.sleep(0.25)

        find_region = {'top': 840, 'left': 1000, 'width': 225, 'height': 100}

        self.find_element(
            'images/trade_mission_give_items_btn.jpeg',
            click_at_accept_btn,
            find_region,
            should_find=False
        )

    def close_trade_mission_window(self):
        def click_at_close_btn(is_first):
            if is_first:
                print("Finding close btn...")
            else:
                print("Can't find close btn")

        find_region = {'top': 15, 'left': 435, 'width': 65, 'height': 55}

        points = self.find_element(
            'images/close_btn.jpeg',
            click_at_close_btn,
            find_region,
        )

        pg.click(*self.get_screen_point(points[0], find_region), duration=0.15)
        pg.move(0, 40, duration=0.15)
        pg.sleep(0.2)

        def check_at_close_btn(is_first):
            if is_first:
                print("Finding close btn...")
            else:
                print("Still found close btn")
                pg.move(0, -40, duration=0.15)
                pg.click()
                pg.move(0, 40, duration=0.15)
                pg.sleep(0.25)

        self.find_element(
            'images/close_btn.jpeg',
            check_at_close_btn,
            find_region,
            should_find=False
        )



if __name__ == '__main__':
    pg.countdown(3)

    print("Finding window...", end='')
    albion_window = WindowCapture()
    # albion_window.init_region('Albion Online Client')
    print(' +')

    ui = TradeHeartsUIController(albion_window)

    # start from bank
    #

    # take mission
    ui.open_trade_mission_window()
    ui.open_trade_mission_tab()
    ui.open_lymhurst_mission()
    ui.open_major_mission_dialog()
    ui.click_contract_accept_btn()

    # give items to shady
    # move to 950 675
    pg.moveTo(*ui.get_screen_point((950, 675), ui.window.getRegion()), duration=0.15)
    ui.open_major_mission_dialog()
    ui.click_contract_give_items_btn()
    ui.close_trade_mission_window()

    # finish mission and give items to yara
    ui.open_major_mission_dialog()
    ui.click_contract_give_items_btn()
    ui.close_trade_mission_window()

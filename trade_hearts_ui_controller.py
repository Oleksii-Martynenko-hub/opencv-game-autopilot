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
        self.default_hsv_filter = HsvFilter(hMin=0, sMin=0, vMin=0, hMax=179, sMax=255, vMax=255, sAdd=0, sSub=0, vAdd=0, vSub=0)

    def get_screen_point(self, point, find_region):
        win_top = self.window.getRegion()['top']
        win_left = self.window.getRegion()['left']
        t, l, w, h = find_region.values()
        region = {'top': win_top + t, 'left': win_left + l, 'width': w, 'height': h}

        rel_pt = cmath.get_relative_point(self.window.getRegion(), region, child_point=point)
        return cmath.get_relative_point(self.screen_region, self.window.getRegion(), child_point=rel_pt)

    def find_element(self, element, not_success_callback, find_region: dict, should_find=True, tries=None, times=None, threshold=0.95, hsv_filter=None):
        is_first = True
        temp = cv.imread(element, cv.IMREAD_UNCHANGED)

        if temp is not None:
            vision = Vision(temp, hsv_filter=hsv_filter or self.default_hsv_filter)

            win_top = self.window.getRegion()['top']
            win_left = self.window.getRegion()['left']
            t, l, w, h = find_region.values()
            region = {'top': win_top + t, 'left': win_left + l, 'width': w, 'height': h}
            
            amount_tries = tries
            amount_times = times

            while True:
                frame = self.window.getScreenshot(region)
                processed = vision.apply_hsv_filter(frame, hsv_filter=hsv_filter or self.default_hsv_filter)

                rectangles = vision.find(processed, threshold=threshold)
                points = vision.get_click_points(rectangles)

                if should_find:
                    if len(points) > 0:
                        print(' +')
                        return points

                    if len(points) <= 0:
                        if amount_tries is not None:
                            amount_tries -= 1
                        not_success_callback(is_first)
                        if is_first:
                            is_first = False
                        if amount_tries is not None and amount_tries <= 0:
                            break

                if not should_find:
                    if len(points) <= 0:
                        print(' +')
                        break

                    if len(points) > 0:
                        if amount_tries is not None:
                            amount_tries -= 1
                        not_success_callback(is_first, points)
                        if is_first:
                            is_first = False
                        if amount_tries is not None and amount_tries <= 0:
                            break

    def open_trade_mission_window(self):
        def click_at_vendor(is_first):
            if is_first:
                print("Opening trade mission window...")
            else:
                print("Can't open trade mission window")
            self.check_is_player_flagged()
            pg.sleep(0.15)

        find_region = {'top': 475, 'left': 475, 'width': 80, 'height': 100}

        points = self.find_element(
            'images/trade_mission_tab.jpeg',
            click_at_vendor,
            find_region,
        )

        pg.moveTo(*self.get_screen_point(points[0], find_region), duration=0.15)

    def check_is_player_flagged(self):
        def click_at_flag_btn(is_first):
            if is_first:
                print("Checking is player flagged...")
            else:
                print("Can't find flag button")
            pg.click()
            pg.sleep(0.15)

        find_region = {'top': 710, 'left': 300, 'width': 170, 'height': 80}

        points = self.find_element(
            'images/faction_flag_btn.jpeg',
            click_at_flag_btn,
            find_region,
            tries=10,
        )

        if points is not None and len(points) > 0:
            pg.moveTo(*self.get_screen_point(points[0], find_region), duration=0.15)

            self.click_flagged_yes_btn()

    def click_flagged_yes_btn(self):
        def click_at_yes_btn(is_first):
            if is_first:
                print("Finding yes btn...")
            else:
                print("Can't find yes btn")
                pg.click()
                pg.sleep(0.15)

        find_region = {'top': 490, 'left': 680, 'width': 250, 'height': 75}

        points = self.find_element(
            'images/faction_flag_yes_btn.jpeg',
            click_at_yes_btn,
            find_region,
        )

        pg.click(*self.get_screen_point(points[0], find_region), duration=0.15)
        pg.move(0, 40, duration=0.15)
        pg.sleep(0.2)

        def click_at_yes_btn(is_first, points=[]):
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
            'images/faction_flag_yes_btn.jpeg',
            click_at_yes_btn,
            find_region,
            should_find=False
        )

        hp_bar_region = {'top': 320, 'left': 860, 'width': 210, 'height': 280}

        pg.moveTo(*self.get_screen_point((99, 154), hp_bar_region), duration=0.15)

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

        def click_at_accept_btn(is_first, points=[]):
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

        def click_at_accept_btn(is_first, points=[]):
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
        print("Finding close btn...")

        def click_at_close_btn(is_first):
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

        def check_at_close_btn(is_first, points=[]):
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

    def open_bank(self):
        def click_at_chest(is_first):
            if is_first:
                print("Opening bank chest...")
            else:
                print("Can't open bank chest")
            pg.click()
            pg.sleep(0.35)

        find_region = {'top': 25, 'left': 25, 'width': 250, 'height': 120}

        points = self.find_element(
            'images/bank_icon.jpeg',
            click_at_chest,
            find_region,
        )

        pg.moveTo(*self.get_screen_point(points[0], find_region), duration=0.15)

    def open_inventory(self):
        print("Opening inventory...")

        def press_inventory_key(is_first):
            print("Can't open inventory")
            pg.press('x')
            pg.sleep(0.35)

        find_region = {'top': 50, 'left': 1530, 'width': 225, 'height': 60}

        points = self.find_element(
            'images/inventory_title.jpeg',
            press_inventory_key,
            find_region,
        )

        pg.moveTo(*self.get_screen_point(points[0], find_region), duration=0.15)

    def put_hearts_to_bank(self):
        def click_with_shift_at_heart(is_first):
            if is_first:
                print("Putting hearts to bank...")
            else:
                print("Can't put hearts to bank")

        find_region = {'top': 550, 'left': 1430, 'width': 460, 'height': 400}

        points = self.find_element(
            'images/treehearts_part.jpeg',
            click_with_shift_at_heart,
            find_region,
            tries=30,
        )

        if points is not None and len(points) > 0:
            pg.moveTo(*self.get_screen_point(points[0], find_region), duration=0.25)
            pg.keyDown('shiftleft')
            pg.sleep(0.15)
            pg.click()
            pg.sleep(0.15)
            pg.keyUp('shiftleft')
            pg.moveTo(*self.get_screen_point((1430, 500), {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}), duration=0.15)
            pg.sleep(0.2)

            def check_hearts_in_inventory(is_first, points=[]):
                if is_first:
                    print("Putting hearts to bank...")
                else:
                    print("Can't find hearts to bank")
                    pg.moveTo(*self.get_screen_point(points[0], find_region), duration=0.25)
                    pg.keyDown('shiftleft')
                    pg.sleep(0.15)
                    pg.click()
                    pg.sleep(0.15)
                    pg.keyUp('shiftleft')
                    pg.moveTo(*self.get_screen_point((1430, 500), {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}),
                              duration=0.15)
                    pg.sleep(0.2)

            self.find_element(
                'images/treehearts_part.jpeg',
                check_hearts_in_inventory,
                find_region,
                should_find=False,
            )

    def take_hearts_to_inventory(self):
        print("Taking hearts to inventory...")

        def click_with_shift_at_heart(is_first):
            print("Can't take hearts to inventory")

        find_region = {'top': 250, 'left': 36, 'width': 550, 'height': 630}

        points = self.find_element(
            'images/beasthearts_15.jpeg',
            click_with_shift_at_heart,
            find_region,
        )
        pg.keyDown('shiftleft')
        pg.sleep(0.15)
        pg.click(*self.get_screen_point(points[0], find_region), duration=0.25)
        pg.sleep(0.15)
        pg.keyUp('shiftleft')
        pg.move(0, 100, duration=0.15)
        pg.sleep(0.2)

        print("Check hearts in inventory...")

        def check_hearts_in_inventory(is_first, points=[]):
            print("Can't take hearts to inventory")
            pg.move(0, -100, duration=0.15)
            pg.keyDown('shift')
            pg.sleep(0.15)
            pg.click()
            pg.sleep(0.15)
            pg.keyUp('shift')
            pg.move(0, 100, duration=0.15)
            pg.sleep(0.5)

        find_region = {'top': 550, 'left': 1430, 'width': 460, 'height': 400}

        points = self.find_element(
            'images/beasthearts_15.jpeg',
            check_hearts_in_inventory,
            find_region,
        )

    def close_bank_window(self):
        print("Finding close btn...")

        def click_at_close_btn(is_first):
            print("Can't find close btn")

        find_region = {'top': 15, 'left': 580, 'width': 65, 'height': 55}

        points = self.find_element(
            'images/close_btn.jpeg',
            click_at_close_btn,
            find_region,
        )

        pg.click(*self.get_screen_point(points[0], find_region), duration=0.15)
        pg.move(0, 40, duration=0.15)
        pg.sleep(0.2)

        def check_at_close_btn(is_first, points=[]):
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
    # ui.click_contract_accept_btn()

    # give items to shady
    # pg.moveTo(*ui.get_screen_point((950, 675), {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}), duration=0.15)
    # ui.open_major_mission_dialog()
    # ui.click_contract_give_items_btn()
    # ui.close_trade_mission_window()
    #
    # # finish mission and give items to yara
    # ui.open_major_mission_dialog()
    # ui.click_contract_give_items_btn()
    # ui.close_trade_mission_window()

    # put award hearts and take another hearts
    # ui.open_bank()
    # ui.open_inventory()
    # ui.put_hearts_to_bank()
    # ui.take_hearts_to_inventory()
    # ui.close_bank_window()

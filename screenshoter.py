

import cv2 as cv
import inquirer
import numpy as np
import pyautogui as pg
from mss import mss, tools
import threading as thr

from key_listener import KeysListener


class Screenshoter:
    screenW = pg.size()[0]
    screenH = pg.size()[1]
    screen_region = dict(top=0, left=0, width=screenW, height=screenH)

    view_region = dict(top=0, left=0, width=screenW, height=screenH)
    default_path = "images/"
    select_color = (0, 255, 0)
    scale_percent = 100
    times = 1

    left_top = None
    right_bottom = None
    hold_l_t = False
    hold_r_b = False

    def __init__(self, path=None, region=None, select_color=None, times=None, scale_percent=None):
        if region is not None:
            self.view_region = region
        if select_color is not None:
            self.select_color = select_color
        if times is not None:
            self.times = times
        if path is not None:
            self.default_path = path
        if scale_percent is not None:
            self.scale_percent = scale_percent

        self.sct = mss()

    def shot(self):
        if self.left_top is not None and self.right_bottom is not None:
            left, top = self.left_top
            right, bottom = self.right_bottom

            grab_region = {"top": top, "left": left, "width": right - left, "height": bottom - top}

            images = []

            for i in range(self.times):
                img = self.sct.grab(grab_region)
                images.append(img)

            print('view_region: ', scrn.view_region)
            print('grab_region: ', grab_region)
            print('scale_percent: ', scrn.scale_percent)

            question_name = [
                inquirer.Text('name', message="How to name screenshot?")
            ]
            question_change_path = [
                inquirer.List('is_change_path', message="Would you like to change the path?", choices=['No', 'Yes']),
            ]

            screenshot = inquirer.prompt(question_name)
            change_path = inquirer.prompt(question_change_path)

            path = ''

            if change_path['is_change_path'] == 'Yes':
                question_path = [
                    inquirer.Text('path', message="Write path without screenshot name!")
                ]
                new_path = inquirer.prompt(question_path)

                path = new_path['path'] + screenshot['name'] + ".jpeg"
            elif change_path['is_change_path'] == 'No':
                path = self.default_path + screenshot['name'] + ".jpeg"

            for i, img in enumerate(images):
                tools.to_png(img.rgb, img.size,  output=i == 0 and path or path.replace('.jpeg', f'{i}.jpeg'))

            print(f'Screenshot saved as - {path}')

    def set_left_top(self, x, y):
        self.left_top = (x, y)

    def set_right_bottom(self, x, y):
        self.right_bottom = (x, y)

    def increase_scale(self):
        self.scale_percent += 5

    def decrease_scale(self):
        self.scale_percent -= 5

    def increase_view(self):
        self.view_region['top'] -= 5
        self.view_region['left'] -= 5
        self.view_region['width'] += 10
        self.view_region['height'] += 10

    def decrease_view(self):
        self.view_region['top'] += 5
        self.view_region['left'] += 5
        self.view_region['width'] -= 10
        self.view_region['height'] -= 10

    def move_view_to_top(self):
        self.view_region['top'] -= 1

    def move_view_to_bottom(self):
        self.view_region['top'] += 1

    def move_view_to_left(self):
        self.view_region['left'] -= 1

    def move_view_to_right(self):
        self.view_region['left'] += 1

    def move_view_to_top_20(self):
        self.view_region['top'] -= 20

    def move_view_to_bottom_20(self):
        self.view_region['top'] += 20

    def move_view_to_left_20(self):
        self.view_region['left'] -= 20

    def move_view_to_right_20(self):
        self.view_region['left'] += 20

    def add_point(self):
        if self.left_top is None:
            if not self.hold_l_t:
                self.hold_l_t = True
            else:
                self.hold_l_t = False
                self.hold_r_b = True

                self.set_left_top(*pg.position())

        elif self.right_bottom is None:
            if not self.hold_r_b:
                self.hold_r_b = True
            else:
                self.hold_r_b = False

                self.set_right_bottom(*pg.position())

    def remove_point(self):
        if self.right_bottom is not None and not self.hold_r_b:
            self.hold_r_b = True
            self.right_bottom = None

        elif self.right_bottom is None and self.hold_r_b:
            self.hold_r_b = False
            self.left_top = None
            self.hold_l_t = True

        elif self.left_top is None and self.hold_l_t:
            self.hold_l_t = False

    @staticmethod
    def get_relative_point(parent_region: dict, child_region: dict, child_point: tuple = None,
                           parent_point: tuple = None):
        left_diff = child_region["left"] - parent_region["left"]
        top_diff = child_region["top"] - parent_region["top"]

        if child_point is not None:
            x, y = child_point
            new_x = x + left_diff
            new_y = y + top_diff

            return new_x, new_y

        if parent_point is not None:
            x, y = parent_point
            new_x = x - left_diff
            new_y = y - top_diff

            return new_x, new_y

    def view(self):
        print("Starting looping...")
        while True:
            frame = np.array(self.sct.grab(self.view_region))

            if self.hold_l_t:
                x, y = pg.position()
                rel_x, rel_y = self.get_relative_point(self.screen_region, self.view_region, parent_point=(x, y))
                frame = cv.line(frame, (rel_x, rel_y), (rel_x + 300, rel_y), self.select_color, 1)
                frame = cv.line(frame, (rel_x, rel_y), (rel_x, rel_y + 300), self.select_color, 1)

            elif self.left_top is not None and self.hold_r_b:
                lt = self.left_top
                x_m, y_m = pg.position()

                rel_l, rel_t = self.get_relative_point(self.screen_region, self.view_region, parent_point=lt)
                rel_m_r, rel_m_b = self.get_relative_point(self.screen_region, self.view_region, parent_point=(x_m, y_m))
                frame = cv.rectangle(frame, (rel_l, rel_t), (rel_m_r, rel_m_b), self.select_color, 1)

            elif self.left_top is not None and self.right_bottom is not None:
                lt = self.left_top
                rb = self.right_bottom
                rel_l, rel_t = self.get_relative_point(self.screen_region, self.view_region, parent_point=lt)
                rel_r, rel_b = self.get_relative_point(self.screen_region, self.view_region, parent_point=rb)
                frame = cv.rectangle(frame, (rel_l, rel_t), (rel_r, rel_b), self.select_color, 1)

            # scale for more efficient select
            if self.scale_percent != 100:
                width = int(frame.shape[1] * self.scale_percent / 100)
                height = int(frame.shape[0] * self.scale_percent / 100)
                dim = (width, height)

                frame = cv.resize(frame, dim)

            cv.imshow("Screenshoter view", frame)

            key = cv.waitKey(1)
            if key == 27:
                break


if __name__ == "__main__":
    region = {'top': 0, 'left': 1183, 'width': 714, 'height': 384}

    scrn = Screenshoter(path='images/location_titles/', region=region, scale_percent=150)

    lsn = KeysListener()

    lsn.add_combination([lsn.Key.cmd, lsn.Key.shift, lsn.KeyCode.from_char('a')], scrn.add_point)
    lsn.add_combination([lsn.Key.cmd, lsn.Key.shift, lsn.KeyCode.from_char('r')], scrn.remove_point)
    lsn.add_combination([lsn.Key.cmd, lsn.Key.shift, lsn.KeyCode.from_char('s')], scrn.shot)

    lsn.add_combination([lsn.Key.up], scrn.move_view_to_top)
    lsn.add_combination([lsn.Key.down], scrn.move_view_to_bottom)
    lsn.add_combination([lsn.Key.left], scrn.move_view_to_left)
    lsn.add_combination([lsn.Key.right], scrn.move_view_to_right)

    lsn.add_combination([lsn.Key.shift, lsn.Key.up], scrn.move_view_to_top_20)
    lsn.add_combination([lsn.Key.shift, lsn.Key.down], scrn.move_view_to_bottom_20)
    lsn.add_combination([lsn.Key.shift, lsn.Key.left], scrn.move_view_to_left_20)
    lsn.add_combination([lsn.Key.shift, lsn.Key.right], scrn.move_view_to_right_20)

    lsn.add_combination([lsn.Key.shift, lsn.KeyCode.from_char('<')], scrn.decrease_view)
    lsn.add_combination([lsn.Key.shift, lsn.KeyCode.from_char('>')], scrn.increase_view)

    lsn.add_combination([lsn.KeyCode.from_char('-')], scrn.decrease_scale)
    lsn.add_combination([lsn.KeyCode.from_char('=')], scrn.increase_scale)

    print('Creating listener thread...', end='')
    listenerT = thr.Thread(target=lsn.listen)
    print(' +')

    print('Starting thread...', end='')
    listenerT.start()

    scrn.view()

    cv.destroyAllWindows()

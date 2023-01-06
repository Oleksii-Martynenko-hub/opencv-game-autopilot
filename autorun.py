import sys

import cv2 as cv
import threading as thr
from math import hypot, sin, cos, atan2

import inquirer as inquirer
import numpy as np
from time import time
import pyautogui as pg

from autorun_routes_service import RoutesService, RouteType
from complete_routes import complete_routes, routes, city_routes
from window_capture import WindowCapture
from vision import Vision
from filters.hsvfilter import HsvFilter
from key_listener import KeysListener
from custom_math import CustomMath as cmath


class AutoRun:
    WINDOW_TRACKBAR_NAME = "Center of player GUI"

    current_position = None
    current_mouse_pt = None
    routes = []
    points = []
    current_point = None
    completed_points = []
    rest_of_points = []

    pause = True
    is_moving = False

    is_checking_player_stack_start_time = None
    reset_time_player_stack = None

    current_map_scale = 1
    current_length = None
    last_position = None
    last_position_for_speed_calc = None
    last_time = None
    speed_list = []
    current_position_list = []
    current_time_list = []

    player_center = None

    points_region = None
    position_region = None

    window: WindowCapture = None
    stopWatching = None

    north_vision: Vision
    arrow_vision: Vision

    screenW = pg.size()[0]
    screenH = pg.size()[1]
    screen_region = dict(top=0, left=0, width=screenW, height=screenH)

    output_frame = None

    def __init__(self, window: WindowCapture = None, routes: list[RouteType] = []):
        self.routes = routes
        self.routes_service = RoutesService()
        if window is not None:
            self.window = window

        # init visions
        print("Init visions...", end='')
        north_temp = cv.imread(
            'images/minimap_north_symbol.jpeg', cv.IMREAD_UNCHANGED)
        minimap_direction_symbols_hsv_filter = HsvFilter.minimap_direction_symbols()
        self.north_vision = Vision(north_temp, hsv_filter=minimap_direction_symbols_hsv_filter)

        arrow_temp = cv.imread(
            'images/minimap_arrow_u_or_comp.jpeg', cv.IMREAD_UNCHANGED)
        minimap_arrow_hsv_filter = HsvFilter.minimap_arrow()
        self.arrow_vision = Vision(arrow_temp, hsv_filter=minimap_arrow_hsv_filter)
        print(' +')

    def find_location(self, location: str):
        location_template = cv.imread(
            f'images/location_titles/{location}.jpeg', cv.IMREAD_UNCHANGED)
        if location_template is None:
            location_template = cv.imread(
                f'images/location_titles/{location}.png', cv.IMREAD_UNCHANGED)

        if location_template is not None:
            location_hsv_filter = HsvFilter.location_minimap_title()
            location_vision = Vision(location_template, hsv_filter=location_hsv_filter)

            t, l, w, h = self.window.getRegion().values()

            region = {"top": t + 15, "left": l + 300, "width": 380, "height": 90}

            find_counter = 0
            while True:
                frame = self.window.getScreenshot(region)
                processed = location_vision.apply_hsv_filter(frame, hsv_filter=location_hsv_filter)
                rectangles = location_vision.find(processed, threshold=0.8)

                if len(rectangles) > 0:
                    find_counter += 1
                    if find_counter > 5:
                        break
                else:
                    find_counter = 0

    def find_opened_map(self):
        t, l, w, h = self.window.getRegion().values()
        north_symbol_region = {'top': t + 108, 'left': l + 800, 'width': 335, 'height': 225}
        frame = self.window.getScreenshot(north_symbol_region)
        processed = self.north_vision.apply_hsv_filter(frame, hsv_filter=self.north_vision.hsv_filter)
        return self.north_vision.find(processed, threshold=0.75)

    def find_mount_up_status(self):
        mount_up_status_template = cv.imread(
            'images/mount_up_status.jpeg', cv.IMREAD_UNCHANGED)

        if mount_up_status_template is not None:
            mount_up_status_hsv_filter = HsvFilter.mount_up_status()
            location_vision = Vision(mount_up_status_template, hsv_filter=mount_up_status_hsv_filter)
            t, l, w, h = self.window.getRegion().values()

            region = {"top": t + 90, "left": l + 90, "width": 240, "height": 100}
            frame = self.window.getScreenshot(region)
            processed = location_vision.apply_hsv_filter(frame, hsv_filter=mount_up_status_hsv_filter)
            return location_vision.find(processed, threshold=0.75)

    def map_open_close_handler(self, open_map=False, close_map=False):
        find_counter = 0
        if open_map:
            print('Opening map...', end='')
            while True:
                rectangles = self.find_opened_map()
                if len(rectangles) > 0:
                    find_counter += 1
                    if find_counter > 5:
                        print(' +')
                        break
                else:
                    find_counter -= 1
                    if find_counter < -5:
                        find_counter = 0
                        pg.keyDown('shiftleft')
                        pg.keyDown('e')
                        pg.keyUp('e')
                        pg.keyUp('shiftleft')
                        pg.sleep(0.4)

        if close_map:
            find_counter = 0
            print('Closing map...', end='')
            while True:
                rectangles = self.find_opened_map()
                if len(rectangles) == 0:
                    find_counter += 1
                    if find_counter > 5:
                        print(' +')
                        break
                else:
                    find_counter -= 1
                    if find_counter < -5:
                        find_counter = 0
                        pg.keyDown('shiftleft')
                        pg.keyDown('e')
                        pg.keyUp('e')
                        pg.keyUp('shiftleft')
                        pg.sleep(0.4)

    def mount_up_down_handler(self, mount_up=False, mount_down=False):
        find_counter = 0
        if mount_up:
            print('Mounting up...', end='')
            while True:
                rectangles = self.find_mount_up_status()
                if len(rectangles) > 0:
                    find_counter += 1
                    if find_counter > 5:
                        print(' +')
                        break
                else:
                    find_counter -= 1
                    if find_counter < -5:
                        find_counter = 0
                        pg.hotkey('a')
                        pg.sleep(3)

        if mount_down:
            find_counter = 0
            print('Mounting down...', end='')
            while True:
                rectangles = self.find_mount_up_status()
                if len(rectangles) == 0:
                    find_counter += 1
                    if find_counter > 5:
                        print(' +')
                        break
                else:
                    find_counter -= 1
                    if find_counter < -5:
                        find_counter = 0
                        pg.hotkey('a')
                        pg.sleep(0.5)

    def find_minimap_points_region(self):
        while self.points_region is None:
            rectangles = self.find_opened_map()

            points = self.north_vision.get_click_points(rectangles)

            if len(points) > 0:
                window_region = self.window.getRegion()
                t, l, w, h = window_region.values()

                north_symbol_region = {'top': t + 108, 'left': l + 800, 'width': 335, 'height': 225}

                x, y = cmath.get_relative_point(window_region, north_symbol_region, child_point=points[0])

                self.points_region = {"top": t + y + 50, "left": l + x - 500, "width": 1000, "height": 700}

    def find_player_center(self, region=None):
        hp_bar_temp = cv.imread(
            'images/player_hp_bar.jpeg', cv.IMREAD_UNCHANGED)
        player_hp_bar_hsv_filter = HsvFilter.player_hp_bar()
        player_hp_vision = Vision(hp_bar_temp, hsv_filter=player_hp_bar_hsv_filter)

        while self.player_center is None:
            t, l, w, h = self.window.getRegion().values()
            region2 = {'top': t + 320, 'left': l + 860, 'width': 210, 'height': 280}
            frame = self.window.getScreenshot(region2)
            processed = player_hp_vision.apply_hsv_filter(frame, hsv_filter=player_hp_bar_hsv_filter)
            rectangles = player_hp_vision.find(processed, threshold=0.95)
            points = player_hp_vision.get_click_points(rectangles)

            if len(points):
                self.player_center = (points[0][0] - 5, points[0][1] + 107)

    # DEBUG METHOD
    def init_center_control_gui(self):
        cv.namedWindow(self.WINDOW_TRACKBAR_NAME, cv.WINDOW_NORMAL)
        cv.resizeWindow(self.WINDOW_TRACKBAR_NAME, 450, 200)

        def nothing(position):
            pass

        cv.createTrackbar("X", self.WINDOW_TRACKBAR_NAME, 0, 30, nothing)
        cv.createTrackbar("Y", self.WINDOW_TRACKBAR_NAME, 0, 30, nothing)
        cv.createTrackbar("Radius", self.WINDOW_TRACKBAR_NAME, 15, 25, nothing)

        cv.setTrackbarPos("X", self.WINDOW_TRACKBAR_NAME, 15)
        cv.setTrackbarPos("Y", self.WINDOW_TRACKBAR_NAME, 15)

    # DEBUG METHOD
    def get_rel_center_from_gui(self):
        center = dict(x=0, y=0, r=10)
        center["x"] = cv.getTrackbarPos("X", self.WINDOW_TRACKBAR_NAME)
        center["y"] = cv.getTrackbarPos("Y", self.WINDOW_TRACKBAR_NAME)
        center["r"] = cv.getTrackbarPos("Radius", self.WINDOW_TRACKBAR_NAME)
        return center

    def init_current_position(self):
        while self.current_position is None:
            self.find_current_position()

    def reset_current_position_region(self, is_mouse=False, is_current_point=False):
        if self.points_region is not None:
            radius = 75
            x = 0
            y = 0

            t, l, w, h = self.points_region.values()

            if is_mouse:
                mouse_x, mouse_y = pg.position()
                x, y = cmath.get_relative_point(self.screen_region, self.points_region, parent_point=(mouse_x, mouse_y))

            elif is_current_point and self.current_point is not None:
                x, y = self.current_point

            region = {
                "top": t + y - radius,
                "left": l + x - radius,
                "width": radius * 2,
                "height": radius * 2,
            }

            self.position_region = region

    def set_position_region_by_mouse_pos(self):
        print('Back up position region by mouse')
        radius = 75
        mouse_x, mouse_y = pg.position()

        x, y = cmath.get_relative_point(self.screen_region, self.points_region, parent_point=(mouse_x, mouse_y))

        t, l, w, h = self.points_region.values()
        region = {
            "top": t + y - radius,
            "left": l + x - radius,
            "width": radius * 2,
            "height": radius * 2,
        }

        self.position_region = region

    def find_current_position(self):
        radius = 75

        region = None
        if self.position_region is not None:
            region = self.position_region

        elif self.current_point and self.points_region is not None:
            t, l, w, h = self.points_region.values()
            x, y = self.current_point
            region = {
                "top": t + y - radius,
                "left": l + x - radius,
                "width": radius * 2,
                "height": radius * 2,
            }

            self.position_region = region

        elif self.points_region is not None:
            region = self.points_region

        frame = self.window.getScreenshot(region)
        processed = self.arrow_vision.apply_hsv_filter(frame, hsv_filter=self.arrow_vision.hsv_filter)
        rectangles = self.arrow_vision.find(processed)
        points = self.arrow_vision.get_click_points(rectangles)
        
        if self.position_region is not None and self.points_region is not None:
            rel_points = []
            for p in points:
                rel_points.append(cmath.get_relative_point(self.points_region, self.position_region, child_point=p))

            self.output_frame = self.arrow_vision.draw_crosshairs(self.output_frame, rel_points)
            self.current_position = rel_points[0] if len(rel_points) else None

        if len(points):
            top = 0
            left = 0

            if self.position_region is None and self.points_region is not None:
                top = self.points_region["top"]
                left = self.points_region["left"]

            if self.position_region is not None:
                top = self.position_region["top"]
                left = self.position_region["left"]

            x, y = points[0]
            self.position_region = {
                "top": top + y - radius,
                "left": left + x - radius,
                "width": radius * 2,
                "height": radius * 2,
            }

    def moving_handler(self):
        if not self.pause:
            if self.current_mouse_pt is not None and self.current_length is not None and self.current_length > round(self.current_map_scale * 3):
                rel_mouse_pt = cmath.get_relative_point(self.screen_region, self.window.getRegion(), child_point=self.current_mouse_pt)
                self.move_to_current_point(rel_mouse_pt)
            elif self.current_length is not None and self.current_length <= round(self.current_map_scale * 3):
                if len(self.rest_of_points) > 0:
                    self.completed_points.append(self.current_point)
                    self.current_point = self.rest_of_points.pop(0)
                else:
                    self.set_pause_of_moving()

                    return True

    def move_to_current_point(self, mouse_pt):
        if self.pause is False and self.is_moving is False:
            self.is_moving = True
            self.map_open_close_handler(close_map=True)
            print('Moving...', end='')
            pg.click(*mouse_pt, button='right', duration=0.2)
            pg.sleep(0.2)
            self.map_open_close_handler(open_map=True)
            self.reset_current_position_region(is_current_point=True)
            pg.hotkey('command', 'a')
            print(' +')
            return

        pg.moveTo(*mouse_pt)

    def unset_pause_of_moving(self):
        if self.pause is True:
            print('Unsetting pause of moving...', end='')
            self.pause = False
            print(' +')

    def set_pause_of_moving(self):
        if self.pause is False:
            print('Setting pause of moving...', end='')
            self.pause = True
            print(' +')

        if self.is_moving is True:
            print('Stopping...', end='')
            self.is_moving = False
            pg.sleep(0.2)
            pg.move(1, 1, duration=0.2)
            pg.move(-1, -1, duration=0.2)
            # pg.mouseUp(button='right', duration=0.2)
            pg.hotkey('command', 'a')
            print(' +')

    def check_for_stacking_player(self, average_speed):
        is_stack = False
        stack_level = 0
        if not self.pause:
            if average_speed is not None and average_speed <= 3:
                if self.is_checking_player_stack_start_time is None:
                    self.is_checking_player_stack_start_time = time()

                if self.is_checking_player_stack_start_time is not None:
                    current_time = time()
                    if current_time - self.is_checking_player_stack_start_time > 16:
                        self.is_checking_player_stack_start_time = None
                        self.reset_time_player_stack = None
                        # is_stack = True

                        self.set_pause_of_moving()
                        pg.sleep(1)
                        self.unset_pause_of_moving()

                    elif current_time - self.is_checking_player_stack_start_time > 13:
                        self.reset_time_player_stack = time()
                        is_stack = True
                        stack_level = 6
                    elif current_time - self.is_checking_player_stack_start_time > 11:
                        self.reset_time_player_stack = time()
                        is_stack = True
                        stack_level = 5
                    elif current_time - self.is_checking_player_stack_start_time > 9:
                        self.reset_time_player_stack = time()
                        is_stack = True
                        stack_level = 4
                    elif current_time - self.is_checking_player_stack_start_time > 7:
                        self.reset_time_player_stack = time()
                        is_stack = True
                        stack_level = 3
                    elif current_time - self.is_checking_player_stack_start_time > 5:
                        self.reset_time_player_stack = time()
                        is_stack = True
                        stack_level = 2
                    elif current_time - self.is_checking_player_stack_start_time > 3:
                        self.reset_time_player_stack = time()
                        is_stack = True
                        stack_level = 1

            if average_speed is not None and average_speed > 3:
                self.is_checking_player_stack_start_time = None
                is_stack = False

            if self.reset_time_player_stack is not None:
                is_stack = True
                current_time = time()
                if current_time - self.reset_time_player_stack > 1:
                    self.reset_time_player_stack = None
        else:
            self.is_checking_player_stack_start_time = None
            self.reset_time_player_stack = None

        return is_stack, stack_level

    def add_mouse_pos_to_points(self):
        x, y = pg.position()
        pt = cmath.get_relative_point(self.screen_region, self.points_region, parent_point=(x, y))
        self.points.append(pt)

    def add_curr_pos_to_points(self):
        if self.current_position is not None:
            self.points.append(self.current_position)

    def save_points_to_route(self, points=[]):
        current_points: list = len(points) > 0 and points or len(self.points) > 0 and self.points or []
        if len(current_points) > 0:
            questions = [
                inquirer.Text('location', message="What's location?"),
                inquirer.Text('from_', message="Where do you go from?"),
                inquirer.Text('to', message="Where do you go to?"),
                inquirer.Text('scale', message="What is scale of location?")
            ]

            new_route: RouteType = inquirer.prompt(questions)

            RoutesService().add_route({
                'location': str(new_route['location']),
                'from_': str(new_route['from_']),
                'to': str(new_route['to']),
                'scale': float(new_route['scale']),
                'points': current_points
            })

    def remove_last_point_in_building_mode(self):
        if len(self.points):
            self.points.pop()

    def get_speed(self, current_time, current_position):
        if current_position is not None:
            self.current_position_list.append(current_position)
            self.current_time_list.append(current_time)

        if len(self.current_position_list) > 30:
            self.current_position_list.pop(0)

        if len(self.current_time_list) > 30:
            self.current_time_list.pop(0)

        if len(self.current_time_list) > 5 and len(self.current_position_list) > 5:
            seconds = self.current_time_list[-1] - self.current_time_list[0]
            length = cmath.get_length_between_two_points(self.current_position_list[-1], self.current_position_list[0])

            return length / seconds if length is not None and seconds is not None else None

    def get_average_speed(self, speed):
        if speed is not None:
            self.speed_list.append(speed)

        if len(self.speed_list) > 10:
            self.speed_list.pop(0)

        if len(self.speed_list) > 0:
            average_speed = sum(self.speed_list) / len(self.speed_list)

            return round(average_speed, 2)

    def draw_line(self, pt1, pt2):
        if pt1 is not None and pt2 is not None:
            cv.line(self.output_frame, pt1, pt2, (255, 255, 255), 2)

    # DEBUG METHOD
    def draw_current_length(self, pt):
        if pt is not None and self.current_length is not None:
            cv.putText(
                self.output_frame,
                f"{round(self.current_length)}px",
                (pt[0] + 5, pt[1] - 5),
                cv.FONT_HERSHEY_TRIPLEX,
                0.5,
                (0, 255, 0),
            )

    # DEBUG METHOD
    def draw_angle(self, pt, angle):
        if pt is not None and self.current_length is not None:
            cv.putText(
                self.output_frame,
                f"{round(angle)}deg",
                (pt[0] + 5, pt[1] - 5),
                cv.FONT_HERSHEY_TRIPLEX,
                0.5,
                (0, 255, 0),
            )

    def draw_average_speed(self,  speed):
        if speed is not None:
            cv.putText(
                self.output_frame,
                f"{speed} px/sec",
                (10, 52),
                cv.FONT_HERSHEY_PLAIN,
                1.2,
                (0, 255, 0),
            )

    # DEBUG METHOD
    def draw_center_and_dead_zone(self, center: dict = None):
        if self.output_frame is not None and self.player_center is not None:
            rel_x = (center["x"] - 15 if center else 0)
            rel_y = (center["y"] - 15 if center else 0)
            rel_r = center["r"] if center else 23

            x, y = self.player_center
            cv.circle(self.output_frame, (x + rel_x, y + rel_y), 1, (0, 0, 255), 1)
            cv.circle(self.output_frame, (x + rel_x, y + rel_y), rel_r, (0, 255, 0), 1)
            cv.line(self.output_frame, (x + rel_x - rel_r, y + rel_y), (x + rel_x + rel_r, y + rel_y), (0, 0, 255), 1)
            cv.line(self.output_frame, (x + rel_x, y + rel_y - rel_r), (x + rel_x, y + rel_y + rel_r), (0, 0, 255), 1)

    def draw_points(self):
        if self.output_frame is not None:
            for i, (x, y) in enumerate(self.rest_of_points):
                cv.circle(self.output_frame, (x, y), 2, (0, 0, 255), 2)
                # number of points = index + 1 + length of completed + 1 current
                cv.putText(self.output_frame, str(i+1+len(self.completed_points)+1), (x + 3, y - 3), cv.FONT_HERSHEY_PLAIN, 0.8, (0, 0, 0), 2)

            for i, (x, y) in enumerate(self.completed_points):
                cv.circle(self.output_frame, (x, y), 2, (0, 255, 0), 2)
                cv.putText(self.output_frame, str(i+1), (x + 3, y - 3), cv.FONT_HERSHEY_PLAIN, 0.8, (0, 0, 0), 2)

            if self.current_point is not None:
                x, y = self.current_point
                cv.circle(self.output_frame, (x, y), 3, (255, 0, 0), 4)
                cv.putText(self.output_frame, str(len(self.completed_points)+1), (x + 3, y - 3), cv.FONT_HERSHEY_PLAIN, 1.2, (0, 0, 0), 2)

    def draw_fps(self):
        if self.output_frame is not None:
            fps = self.window.getAverageFps()
            cv.putText(self.output_frame, str(fps) + ' fps', (10, 22), cv.FONT_HERSHEY_PLAIN, 1.2, (0, 255, 0), 2)

    # TODO: draw common length?, speed? and rest of time

    def show_output(self):
        if self.output_frame is not None:
            cv.imshow("Autorun output frame", self.output_frame)

    def start(self):
        pg.sleep(0.5)

        # print("Finding player center...", end='')
        # self.find_player_center()
        # print(' +')
        # print("player_center", self.player_center)
        self.player_center = (99, 154)
        t, l, w, h = self.window.getRegion().values()
        hp_bar_region = {'top': t + 320, 'left': l + 860, 'width': 210, 'height': 280}
        self.player_center = cmath.get_relative_point(self.window.getRegion(), hp_bar_region, child_point=self.player_center)
        print("player_center", self.player_center)

        # open the map
        pg.PAUSE = 0
        pg.DARWIN_CATCH_UP_TIME = 0.005

        self.map_open_close_handler(open_map=True)
        pg.sleep(0.5)

        print("Finding map region...", end='')
        self.find_minimap_points_region()
        print(' +')

        for route in self.routes:
            location, from_, to, scale, points = route.values()

            print(f' --- {location} : {from_} --> {to} ---')

            self.points = points
            self.current_map_scale = scale

            pg.sleep(1.5)
            self.map_open_close_handler(open_map=True)

            print('Finding current location...', end='')
            self.find_location(location)
            print(' +')

            # TODO: closest point
            self.rest_of_points = self.points[2:]
            self.current_point = self.points[1]
            self.completed_points = []

            print("Init current position and region...", end='')
            self.position_region = None
            self.init_current_position()
            print(' +')

            # DEBUG LINES
            # print("Debug: Init center control gui...")
            # self.init_center_control_gui()

            self.map_open_close_handler(close_map=True)
            self.mount_up_down_handler(mount_up=True)

            self.unset_pause_of_moving()

            print("Start looping...", end='')
            self.last_time = time()
            self.last_position = self.current_position
            print(' +')
            while True:
                self.output_frame = self.window.getScreenshot(self.points_region)

                self.last_position = self.current_position if self.current_position is not None else self.last_position

                self.find_current_position()

                current_time = time()
                self.last_time = current_time
                current_position = self.current_position if self.current_position is not None else self.last_position

                speed = self.get_speed(current_time, current_position)
                average_speed = self.get_average_speed(speed)
                self.draw_average_speed(average_speed)

                self.draw_line(current_position, self.current_point)

                self.current_length = cmath.get_length_between_two_points(current_position, self.current_point)

                is_player_stack, stack_level = self.check_for_stacking_player(average_speed)

                extra_angle = stack_level == 1 and 50 or \
                              stack_level == 2 and -50 or \
                              stack_level == 3 and 85 or \
                              stack_level == 4 and -85 or \
                              stack_level == 5 and 130 or \
                              stack_level == 6 and -130 or 0
                angle = cmath.get_angle_between_two_points(self.current_point, current_position)

                self.current_mouse_pt = cmath.get_second_point_in_direction(
                    self.player_center,
                    26,
                    is_player_stack and angle + extra_angle or angle
                ) if angle else None

                is_finished_current_points = self.moving_handler()
                if is_finished_current_points:
                    break

                self.draw_line(self.player_center, self.current_mouse_pt)

                # DEBUG LINES
                # center = self.get_rel_center_from_gui()
                self.draw_center_and_dead_zone()

                self.draw_points()

                self.draw_fps()

                self.show_output()

                key = cv.waitKey(1)
                if key == 27:
                    sys.exit()

        # if not building_mode:
            # stop_watching()
            # DEBUG LINES
            # center = self.get_rel_center_from_gui()
            # print("get_rel_center_from_gui: ", center)


if __name__ == '__main__':
    # TODO:
    #  1. Add scale of map to routes
    #  2. Find closest point on map for staring from it
    #  3. Find location from all in routes and starting from it#

    routes_service = RoutesService()

    current_routes_list = [
        *complete_routes.bridgewatch__martlock,
        # *complete_routes.bridgewatch__hornbeam_wood__treeheart_mission,
        # *complete_routes.hornbeam_wood__bridgewatch__treeheart_mission,


        # routes.lazygrass_plain__snapshaft_trough__bridgewatch
    ]

    print("Finding window...", end='')
    albion_window = WindowCapture()
    # albion_window.init_region('Albion Online Client')
    print(' +')
    stop_watching = albion_window.startWatchdogOnActive()

    autorun = AutoRun(window=albion_window, routes=current_routes_list)

    lsn = KeysListener()

    lsn.add_combination([lsn.Key.cmd, lsn.Key.shift, lsn.KeyCode.from_char('z')], autorun.set_pause_of_moving)
    lsn.add_combination([lsn.Key.cmd, lsn.Key.shift, lsn.KeyCode.from_char('x')], autorun.unset_pause_of_moving)
    lsn.add_combination([lsn.Key.cmd, lsn.Key.shift, lsn.KeyCode.from_char('d')], autorun.reset_current_position_region, is_current_point=True)
    lsn.add_combination([lsn.Key.cmd, lsn.Key.shift, lsn.KeyCode.from_char('m')], autorun.set_position_region_by_mouse_pos)

    lsn.add_combination([lsn.Key.cmd, lsn.Key.shift, lsn.KeyCode.from_char('a')], autorun.add_mouse_pos_to_points)
    lsn.add_combination([lsn.Key.cmd, lsn.Key.shift, lsn.KeyCode.from_char('c')], autorun.add_curr_pos_to_points)
    lsn.add_combination([lsn.Key.cmd, lsn.Key.shift, lsn.KeyCode.from_char('r')], autorun.remove_last_point_in_building_mode)
    lsn.add_combination([lsn.Key.cmd, lsn.Key.shift, lsn.KeyCode.from_char('s')], autorun.save_points_to_route)

    print('Creating thread...', end='')
    listenerT = thr.Thread(target=lsn.listen)
    print(' +')

    print('Starting thread...', end='')
    listenerT.start()
    # moving_handlerT.start()
    print(' +')

    autorun.start()

    print('Points: ', autorun.points)

    if stop_watching is not None:
        stop_watching()
    pg.press('esc')
    cv.destroyAllWindows()

    # TODO: Process of choosing routes:
    #  1. Ask name of route/complex of routes
    #  2. Search and show variants of comparison and choose one

    # TODO: Fully autorun process:
    #  0. Choose the route/routes
    #  + 1. find window
    #  + 2. Init all autorun routes
    #  + 3. Find first location (or any of location for possibility start run in the middle)
    #  + 4. If we are on mount, mount down
    #  + 5. Find center of player move control
    #  + 6. Mount up (with additional checks)
    #  + 7. Open and find map region
    #  + 8. Find current position (blue arrow) and position region
    #  9. Calc the closest point, and make it as current (also remove from rest_of_points)
    #       (?? if you right between two, you should choose next instead the closest)
    #  + 10. Close map, start move, open map #

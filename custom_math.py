from math import hypot, sin, cos, atan2
import numpy as np


class CustomMath:

    def __init__(self):
        self.math = 'math'

    @staticmethod
    def get_relative_point(parent_region: dict, child_region: dict, child_point: tuple = None, parent_point: tuple = None):
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

    @staticmethod
    def get_length_between_two_points(pt1, pt2):
        if pt1 is None or pt2 is None:
            return None

        from_x, from_y = pt1
        to_x, to_y = pt2

        side1 = from_x - to_x
        side2 = from_y - to_y

        return hypot(side1, side2)

    @staticmethod
    def get_second_point_in_direction(pt1, length, angle):
        (x2, y2) = (pt1[0] + length * cos(np.deg2rad(angle)), pt1[1] + length * sin(np.deg2rad(angle)))
        return int(x2), int(y2)

    @staticmethod
    def get_angle_between_two_points(pt1, pt2):
        if pt1 is not None and pt2 is not None:
            radians = atan2(pt1[1] - pt2[1], pt1[0] - pt2[0])
            degrees = np.rad2deg(radians)
            if degrees < 0:
                degrees = 180 + 180 - abs(degrees)
            return degrees

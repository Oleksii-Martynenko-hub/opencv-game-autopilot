import cv2 as cv
import numpy as np
import math

# TODO: Trigonometric Functions
#  Known           |  Calculated
#  ________________________________
#  angle = 30deg   |  hypotenuse = 5 / sin(30) = 10
#  opposite = 5    |  adjacent = 5 / tan(30) = 8.66
#  --------------------------------
#  angle = 30deg   |  hypotenuse = 8.66 / cos(30) = 10
#  adjacent = 8.66 |  opposite = 8.66 * tan(30) = 5
#  --------------------------------
#  angle = 30deg   |  opposite = 10 * sin(30) = 5
#  hypotenuse = 10 |  adjacent = 10 * cos(30) = 8.66
#  --------------------------------
#  opposite = 5    |  angle = asin(5 / 10) = 30
#  hypotenuse = 10 |
#  --------------------------------
#  adjacent = 8.66 |  angle = acos(8.66 / 10) = 30
#  hypotenuse = 10 |
#  --------------------------------
#  opposite = 5    |  angle = atan(5 / 8.66) = 30
#  adjacent = 8.66 |
#  --------------------------------#


def get_length_between_two_points(pt1, pt2):
    if pt1 is None or pt2 is None:
        return None

    from_x, from_y = pt1
    to_x, to_y = pt2

    side1 = from_x - to_x
    side2 = from_y - to_y

    return math.hypot(side1, side2)


def get_second_point_in_direction(pt1, length, angle):
    (x2, y2) = (pt1[0] + length * math.cos(np.deg2rad(angle)), pt1[1] + length * math.sin(np.deg2rad(angle)))
    return int(x2), int(y2)


def get_angle_between_two_points(pt1, pt2):
    if pt1 is not None and pt2 is not None:
        radians = math.atan2(pt1[1] - pt2[1], pt1[0] - pt2[0])
        degrees = np.rad2deg(radians)
        if degrees < 0:
            degrees = 180 + 180 - abs(degrees)
        return degrees


def run():
    lightline_length = 2800

    hypotenuse = 590
    base = 370
    opposite = round(base / 2)

    rad_angle = math.asin(opposite / hypotenuse)
    median = round(hypotenuse * math.cos(rad_angle))

    h_angle = round(math.degrees(rad_angle) * 2, 2)
    s_angle = (180 - h_angle) / 2

    height_of_light_begin = 57

    print(median, h_angle, s_angle)

    img = np.zeros((650, 650, 3), dtype=np.uint8)

    p1 = (round(650 / 2), 40)
    p2 = (round(650 / 2) - opposite, median + 40)
    p3 = (round(650 / 2) + opposite, median + 40)

    cv.line(img, p1, p2, (0, 255, 0), 2)
    cv.line(img, p2, p3, (0, 255, 0), 2)
    cv.line(img, p1, p3, (0, 255, 0), 2)

    p_l1 = get_second_point_in_direction(p2, height_of_light_begin, -s_angle)
    cv.line(img, p3, p_l1, (0, 0, 255), 2)

    main_angle = get_angle_between_two_points(p3, p_l1)
    print(main_angle)

    # centroid = ((p1[0] + p2[0] + p3[0]) // 3, (p1[1] + p2[1] + p3[1]) // 3)
    #
    # cv.circle(img, centroid, 4, (0, 255, 0))
    lines = [(p3, p_l1)]
    heights = []

    for i in range(20):
        # length_of_prev_line = math.sin(math.radians(s_angle)) * (base if i == 0 else ) / math.sin(
        #     math.radians(180 - s_angle - main_angle))
        length_of_prev_line = get_length_between_two_points(lines[i][1], lines[i][0])

        curr_base_length = math.sin(math.radians(s_angle - main_angle)) * length_of_prev_line / math.sin(
            math.radians(180 - s_angle))

        curr_line_length = math.sin(math.radians(s_angle)) * curr_base_length / math.sin(
            math.radians(180 - s_angle - main_angle))

        curr_p_l2 = get_second_point_in_direction(lines[i][1], curr_line_length, -main_angle if i % 2 == 0 else 180 + main_angle)
        lines.append((lines[i][1], (curr_p_l2[0] + 1 if i % 2 != 0 else curr_p_l2[0], curr_p_l2[1])))
        cv.line(img, lines[i][1], curr_p_l2, (0, 0, 255), 2)

        height = round(math.sin(math.radians(main_angle * 2)) * length_of_prev_line / math.sin(
            math.radians(180 - s_angle)))
        heights.append(height)
        cv.putText(img, str(height), (lines[i][0][0] + 10 if i % 2 == 0 else lines[i][0][0] - 40, lines[i][0][1]), cv.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)

    common_length = 0

    for line in lines[1:]:
        common_length += get_length_between_two_points(*line)

    print('common length: ', common_length)
    print('heights: ', heights)

    while True:

        cv.imshow("Frame blank", img)

        key = cv.waitKey(1)
        if key == 27:
            break


if __name__ == '__main__':
    run()
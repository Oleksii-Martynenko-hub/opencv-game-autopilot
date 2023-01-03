
import cv2
import numpy
from time import time
import cv2 as cv
import mss
import pyautogui
import threading as thr

from filters.edgefilter import EdgeFilter
from filters.hsvfilter import HsvFilter
from key_listener import KeysListener
from vision import Vision
from window_capture import WindowCapture


def start():
    while True:
        frame = WindowCapture.grabShot(dict(top=300, left=600, width=960, height=540))

        cv.imshow("Test window", frame)

        key = cv.waitKey(1)
        if key == 27:
            pyautogui.countdown(5)
            break


def pause_moving():
    print('set_pause_of_moving')


def start_moving():
    print('unset_pause_of_moving')


def run():
    # ch = cv.imread('images/cats/chewie.jpg', cv.IMREAD_UNCHANGED)
    img = numpy.zeros((650, 650, 3), dtype=numpy.uint8)

    # Create a black window of 400 x 300
    # img = np.zeros((height, width, 3), np.uint8)

    # Three vertices(tuples) of the triangle
    p1 = (int(650/2), 70)
    p2 = (int(650/2) - int(370/2), 600)
    p3 = (int(650/2) + int(370/2), 600)

    # Drawing the triangle with the help of lines
    #  on the black window With given points
    # cv2.line is the inbuilt function in opencv library
    img = cv2.line(img, p1, p2, (0, 255, 0), 2)
    cv2.line(img, p2, p3, (0, 255, 0), 2)
    cv2.line(img, p1, p3, (0, 255, 0), 2)

    # finding centroid using the following formula
    # (X, Y) = (x1 + x2 + x3//3, y1 + y2 + y3//3)
    centroid = ((p1[0] + p2[0] + p3[0]) // 3, (p1[1] + p2[1] + p3[1]) // 3)

    # Drawing the centroid on the window
    cv2.circle(img, centroid, 4, (0, 255, 0))
    # gray = cv.cvtColor(ch, cv.COLOR_BGR2GRAY)

    # vision = Vision(ch)
    #
    # vision.init_control_gui()

    # ch_filter = HsvFilter(hMin=0, sMin=0, vMin=80, hMax=255, sMax=255, vMax=219, sAdd=0, sSub=255, vAdd=0, vSub=22)
    # ch_canny = EdgeFilter(kernelSize=2, erodeIter=0, dilateIter=0, canny1=126, canny2=190)
    # named_win = "Filters"
    # cv.namedWindow(named_win, cv.WINDOW_NORMAL)
    # cv.resizeWindow(named_win, 400, 250)
    #
    # def nothing(position):
    #     pass
    #
    # cv.createTrackbar('d', named_win, 0, 50, nothing)
    # cv.createTrackbar('sigmaColor', named_win, 0, 100, nothing)
    # cv.createTrackbar('sigmaSpace', named_win, 0, 100, nothing)
    # cv.createTrackbar('thresh', named_win, 0, 255, nothing)
    # cv.createTrackbar('maxval', named_win, 0, 255, nothing)
    # # Set default value for Max HSV trackbars
    # cv.setTrackbarPos('d', named_win, 10)
    # cv.setTrackbarPos('sigmaColor', named_win, 35)
    # cv.setTrackbarPos('sigmaSpace', named_win, 25)
    # cv.setTrackbarPos('thresh', named_win, 125)
    # cv.setTrackbarPos('maxval', named_win, 255)

    while True:
        # d = cv.getTrackbarPos('d', named_win)
        # sigmaColor = cv.getTrackbarPos('sigmaColor', named_win)
        # sigmaSpace = cv.getTrackbarPos('sigmaSpace', named_win)
        # thresh = cv.getTrackbarPos('thresh', named_win)
        # maxval = cv.getTrackbarPos('maxval', named_win)
        #
        # filtered = vision.apply_hsv_filter(ch, ch_filter)
        # canny = vision.apply_edge_filter(filtered, ch_canny)
        #
        # blur = cv.bilateralFilter(gray,  d=d, sigmaColor=sigmaColor, sigmaSpace=sigmaSpace)
        # ret, thresh = cv.threshold(blur,  thresh=thresh, maxval=maxval, type=cv.THRESH_BINARY)

        cv.imshow("Frame blank", img)
        # cv.imshow("Frame thresh", thresh)

        key = cv.waitKey(1)
        if key == 27:
            break


if __name__ == '__main__':

    # lsn = KeysListener()
    #
    # print('Adding combs...')
    # lsn.add_combination([lsn.Key.cmd, lsn.KeyCode.from_char('p')], set_pause_of_moving)
    # lsn.add_combination([lsn.Key.cmd, lsn.Key.shift, lsn.KeyCode.from_char('p')], unset_pause_of_moving)
    #
    # # pyautogui.move(100, 100)
    # print('Creating thread...')
    # listenerT = thr.Thread(target=lsn.listen)
    #
    # print('Starting thread...')
    # listenerT.start()
    #
    # print('Running cv loop...')
    # start()
    run()



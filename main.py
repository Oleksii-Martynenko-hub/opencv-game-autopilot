import cv2 as cv
import threading as thr
import queue

from window_capture import WindowCapture
from vision import Vision
from filters.hsvfilter import HsvFilter

north_temp = cv.imread(
    'images/minimap_north_symbol.jpeg', cv.IMREAD_UNCHANGED)
west_temp = cv.imread(
    'images/minimap_west_symbol.jpeg', cv.IMREAD_UNCHANGED)
# _, w, h = temp.shape[::-1]

minimap_direction_symbols_hsv_filter = HsvFilter.minimap_direction_symbols()
# minimap_arrow_hsv_filter = HsvFilter(102, 252, 118, 107, 255, 255, 126, 0, 31, 0)

win = WindowCapture('Albion Online Client')
stopWatching = win.startWatchdogOnActive()


def find_object(vision, hsv_filter=None):

    while True:
        print("findingQ.get()", findingQ.get())
        # if not findingQ.get():
        #     break

        if not frameQ.empty():
            frame = frameQ.get()
            print("frame")

            processed = vision.apply_hsv_filter(frame, hsv_filter=hsv_filter)

            rectangles = vision.find(processed)

            output = vision.draw_rectangles(frame, rectangles)
            print("put output")
            outputQ.put(output)


t, l, w, h = win.getRegion().values()

region = {"top": t + 100, "left": l + 400,
          "width": w - 400 * 2, "height": h - 200}


findingQ = queue.Queue()

frameQ = queue.Queue()
outputQ = queue.Queue()


def run():
    findingQ.put(True)

    north_vision = Vision(north_temp, hsv_filter=minimap_direction_symbols_hsv_filter)
    find_worth = thr.Thread(target=find_object, args=(north_vision, minimap_direction_symbols_hsv_filter))

    while True:
        find_worth.run()
        #     # if not win.isWindowActive:
        #     #     win.win.activate()
        # cv.imshow("Searching img", vision.template_original)

        frame = win.getScreenshot(region)
        print("put frame")
        frameQ.put(frame)

        # processed = vision.apply_hsv_filter(frame)

        # rectangles = vision.find(processed)
        #
        # output = vision.draw_rectangles(frame, rectangles)

        # points = vision.get_click_points(rectangles)
        #
        # output = vision.draw_crosshairs(processed, points)

        win.getAverageFps()

        if not outputQ.empty():
            output = outputQ.get()
            print("output")
            cv.imshow("Frame Albion Online Client", output)

        key = cv.waitKey(1)
        if key == 27:
            findingQ.put(False)
            break


if __name__ == '__main__':
    run()

stopWatching()

cv.destroyAllWindows()

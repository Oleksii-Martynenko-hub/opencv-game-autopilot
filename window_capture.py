import pywinctl as pwc
from mss import mss
import numpy as np
from time import time
from collections.abc import Callable
from collections import namedtuple


class WindowCapture:

    # properties
    last_time = time()
    time_list = []
    win = None
    isWindowActive = False
    sct = None
    w = 0
    h = 0
    l = 0
    t = 0

    def __init__(self, window_name='Albion Online Client'):
        windows = pwc.getWindowsWithTitle(window_name)
        if windows:
            self.win = windows[0]
        if not self.win:
            raise Exception('Window not found: {}'.format(window_name))

        titlebar_height = 28
        self.w, self.h = self.win.size.width, self.win.size.height - titlebar_height
        self.l, self.t = self.win.topleft.x, self.win.topleft.y + titlebar_height

        self.sct = mss()

    def getRegion(self):

        return {"top": self.t, "left": self.l, "width": self.w, "height": self.h}

    def startWatchdogOnActive(self):
        def activeCB(active):
            self.isWindowActive = active

        self.win.watchdog.start(isActiveCB=activeCB)

        return self.win.watchdog.stop

    def getScreenshot(self, region=None):
        reg = region
        if reg is None:
            reg = self.getRegion()

        return np.array(self.sct.grab(reg))

    @staticmethod
    def grabShot(region=None):
        return np.array(mss().grab(region))

    def getAverageFps(self):
        loop_time = 1 / (time() - self.last_time)
        self.time_list.append(loop_time)

        if len(self.time_list) > 100:
            self.time_list.pop(0)

        average_fps = sum(self.time_list) / len(self.time_list)

        self.last_time = time()

        return round(average_fps)

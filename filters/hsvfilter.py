
# custom data structure to hold the state of an HSV filter
class HsvFilter:

    def __init__(self, hMin=None, sMin=None, vMin=None, hMax=None, sMax=None, vMax=None,
                    sAdd=None, sSub=None, vAdd=None, vSub=None):
        self.hMin = hMin
        self.sMin = sMin
        self.vMin = vMin
        self.hMax = hMax
        self.sMax = sMax
        self.vMax = vMax
        self.sAdd = sAdd
        self.sSub = sSub
        self.vAdd = vAdd
        self.vSub = vSub

    @classmethod
    def minimap_arrow(cls):
        return cls(hMin=102, sMin=252, vMin=118, hMax=107, sMax=255, vMax=255, sAdd=126, sSub=0, vAdd=31, vSub=0)

    @classmethod
    def minimap_direction_symbols(cls):
        return cls(hMin=9, sMin=243, vMin=99, hMax=12, sMax=252, vMax=110, sAdd=100, sSub=0, vAdd=30, vSub=0)

    @classmethod
    def player_hp_bar(cls):
        return cls(hMin=19, sMin=242, vMin=140, hMax=120, sMax=255, vMax=255, sAdd=114, sSub=0, vAdd=12, vSub=0)

    @classmethod
    def location_minimap_title(cls):
        return cls(hMin=10, sMin=180, vMin=183, hMax=18, sMax=195, vMax=255, sAdd=65, sSub=0, vAdd=17, vSub=0)

    @classmethod
    def mount_up_status(cls):
        return cls(hMin=19, sMin=75, vMin=59, hMax=109, sMax=255, vMax=250, sAdd=76, sSub=0, vAdd=21, vSub=0)

    @classmethod
    def mount_up_status_black(cls):
        return cls(hMin=5, sMin=12, vMin=25, hMax=120, sMax=240, vMax=90, sAdd=75, sSub=0, vAdd=23, vSub=0)

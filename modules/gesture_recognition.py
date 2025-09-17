from overlay.overlay_regions import REGIONS

class GestureRecognizer:
    def __init__(self):
        self.regions = REGIONS

    def detect_hover(self, fingertip):
        x, y = fingertip
        for name, (x1, y1, x2, y2) in self.regions.items():
            if x1 <= x <= x2 and y1 <= y <= y2:
                return name
        return None

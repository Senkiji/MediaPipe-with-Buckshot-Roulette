import cv2
from overlay.overlay_regions import REGIONS
from overlay.overlay_utils import draw_region

class OverlayManager:
    def draw(self, frame, hovered_region=None, fingertip=None):
        h, w, _ = frame.shape

        # วาดทุก region
        for name, (x1, y1, x2, y2) in REGIONS.items():
            highlight = (name == hovered_region)
            draw_region(frame, (int(x1*w), int(y1*h), int(x2*w), int(y2*h)), name, highlight)

        # วาดจุด fingertip
        if fingertip:
            fx, fy = int(fingertip[0]*w), int(fingertip[1]*h)
            cv2.circle(frame, (fx, fy), 10, (0, 255, 255), -1)

        return frame

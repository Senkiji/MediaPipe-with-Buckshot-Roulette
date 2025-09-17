import cv2

def draw_region(frame, region, name, highlight=False):
    x1, y1, x2, y2 = region
    color = (0, 255, 0) if highlight else (0, 0, 255)
    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
    cv2.putText(frame, name, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

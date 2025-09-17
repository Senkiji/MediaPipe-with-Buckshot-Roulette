import cv2

# กำหนด Layout Region ตามภาพที่ให้มา
REGIONS = {
    "Use Item1": (50, 50, 200, 200),
    "Use Item2": (210, 50, 360, 200),
    "Dealer": (370, 50, 610, 200),
    "Use Item3": (620, 50, 770, 200),
    "Use Item4": (780, 50, 930, 200),
    "Use Item5": (50, 210, 200, 360),
    "Use Item6": (210, 210, 360, 360),
    "You/Grab Item": (370, 210, 610, 360),
    "Use Item7": (620, 210, 770, 360),
    "Use Item8": (780, 210, 930, 360),
}

def draw_layout(frame):
    """
    วาด Layout Overlay บนกล้อง
    """
    for name, (x1, y1, x2, y2) in REGIONS.items():
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, name, (x1 + 10, y1 + 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

def detect_region(x, y):
    """
    ตรวจสอบว่า (x,y) อยู่ใน Region ไหน
    """
    for name, (x1, y1, x2, y2) in REGIONS.items():
        if x1 <= x <= x2 and y1 <= y <= y2:
            return name
    return None

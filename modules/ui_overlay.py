import cv2

# กำหนดตำแหน่ง Layout (x1, y1, x2, y2)
LAYOUT = {
    "Grab Item": (768, 750, 1152, 1000),
    "Grab Gun": (768, 270, 1152, 550),
    
    "You":(768, 550, 1152, 750),
    "Dealer": (768, 100, 1152, 270),

    "Place Item1": (100, 100, 450, 270),
    "Place Item2": (450, 100, 768, 270),
    "Place Item3": (1152, 100, 1450, 270),
    "Place Item4": (1450, 100, 1820, 270),
    "Use Item1": (100,  270, 450, 500),
    "Use Item2": (450, 270, 768, 500),
    "Use Item3": (1152, 270, 1450,500),
    "Use Item4": (1450, 270, 1820,500),

    "Place Item5": (100, 700, 450, 1000),
    "Place Item6": (450, 700, 768, 1000),
    "Place Item7": (1152, 700, 1450, 1000),
    "Place Item8": (1450, 700, 1820, 1000),
    "Use Item5": (100, 500, 450, 700),
    "Use Item6": (450, 500, 768, 700),
    "Use Item7": (1152, 500, 1450, 700),
    "Use Item8": (1450, 500, 1820, 700),
}

def draw_layout(frame):
    """
    วาด Layout บน frame
    """
    for name, (x1, y1, x2, y2) in LAYOUT.items():
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, name, (x1 + 5, y1 + 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

def detect_region(x, y):
    """
    ตรวจว่า point (x, y) อยู่ใน Region ไหน
    """
    for name, (x1, y1, x2, y2) in LAYOUT.items():
        if x1 <= x <= x2 and y1 <= y <= y2:
            return name
    return None

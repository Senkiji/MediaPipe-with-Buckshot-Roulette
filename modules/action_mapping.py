import pyautogui
import time

ACTION_MAP = {
    "Dealer": lambda: pyautogui.click(x=963, y=211),   # ยิง Dealer
    "Grab Gun": lambda: pyautogui.click(x=908, y=600), # หยิบปืน
    "Grab Item": lambda: pyautogui.click(x=958, y=643), # หยิบไอเทม
    "You": lambda: pyautogui.click(x=952, y=830),    #ยิง You

    "Place Item1": lambda: pyautogui.click(385, 252), # วางItem
    "Use Item1": lambda: pyautogui.click(x=480, y=448),

    "Place Item2": lambda: pyautogui.click(606, 241), # วางItem
    "Use Item2": lambda: pyautogui.click(x=668, y=458),

    "Place Item3": lambda: pyautogui.click(1267, 229), # วางItem
    "Use Item3": lambda: pyautogui.click(x=1222, y=436),

    "Place Item4": lambda: pyautogui.click(1491, 218), # วางItem
    "Use Item4": lambda: pyautogui.click(x=1411, y=437),

    "Place Item5": lambda: pyautogui.click(288, 514), # วางItem
    "Use Item5": lambda: pyautogui.click(x=373, y=674),

    "Place Item6": lambda: pyautogui.click(548, 519), # วางItem
    "Use Item6": lambda: pyautogui.click(x=598, y=675),

    "Place Item7": lambda: pyautogui.click(1346, 497), # วางItem
    "Use Item7": lambda: pyautogui.click(x=1300, y=666),

    "Place Item8": lambda: pyautogui.click(1581, 531), # วางItem
    "Use Item8": lambda: pyautogui.click(x=1522, y=668),
}

_last_region = None
_last_time = 0
_delay = 2.0   # Hover 1 วิก่อน Trigger

def perform_action(region):
    global _last_region, _last_time
    now = time.time()

    if region != _last_region:
        _last_region = region
        _last_time = now
        return

    if now - _last_time >= _delay:
        if region in ACTION_MAP:
            print(f"Trigger: {region}")
            ACTION_MAP[region]()
        _last_time = now

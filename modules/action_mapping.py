import pyautogui
import time

ACTION_MAP = {
    "Dealer": lambda: pyautogui.click(button="left"),   # ยิง
    "You/Grab Item": lambda: pyautogui.rightClick(),    # หยิบไอเทม
    "Use Item1": lambda: pyautogui.moveTo(100, 500),
    "Use Item2": lambda: pyautogui.moveTo(200, 500),
    "Use Item3": lambda: pyautogui.moveTo(300, 500),
    "Use Item4": lambda: pyautogui.moveTo(400, 500),
    "Use Item5": lambda: pyautogui.moveTo(500, 500),
    "Use Item6": lambda: pyautogui.moveTo(600, 500),
    "Use Item7": lambda: pyautogui.moveTo(700, 500),
    "Use Item8": lambda: pyautogui.moveTo(800, 500),
}

_last_region = None
_last_time = 0
_delay = 1.0   # Hover 1 วิก่อน Trigger

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

import pyautogui

class MouseController:
    def execute_action(self, action):
        if action == "click":
            pyautogui.click()
        elif action == "right_click":
            pyautogui.rightClick()
        elif action == "reload":
            pyautogui.press("r")
        elif action == "shoot":
            pyautogui.press("space")
        elif action == "next":
            pyautogui.press("enter")

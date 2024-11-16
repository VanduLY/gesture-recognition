import pyautogui

def execute_command(gesture):
    if gesture == "swipe_left":
        pyautogui.press("left")
    elif gesture == "swipe_right":
        pyautogui.press("right")
    elif gesture == "pause":
        pyautogui.press("space")

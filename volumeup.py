import pyautogui
import time

def set_volume_to_80():
    # First, mute the system volume to ensure a consistent starting point
    for _ in range(50):
        pyautogui.press("volumedown")
        time.sleep(0.1)

    # Now, increase the volume to 80% by pressing volume up key 40 times
    for _ in range(40):
        pyautogui.press("volumeup")
        time.sleep(0.1)

if __name__ == "__main__":
    set_volume_to_80()
    print("System volume set to 80%")

import pyautogui
import time


def keep_awake():
    print("Running, press Ctrl+C to stop.")
    while True:
        # Simulate mouse movement
        pyautogui.moveRel(0, 70)
        pyautogui.moveRel(0, -60)

        # Simulate pressing the 'shift' key
        pyautogui.press('shift')

        # Wait for number minutes before repeating actions
        time.sleep(30)


if __name__ == "__main__":
    try:
        keep_awake()
    except KeyboardInterrupt:
        print("Program stopped manually.")

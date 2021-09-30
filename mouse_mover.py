import pyautogui
import time
import threading

pyautogui.FAILSAFE = False
def wiggle():
    def pos():
        pos = pyautogui.position()
        return pos

    while True:
        try:
            position = pos()
            pyautogui.moveRel(0,50, duration=1)
            print(f'Moved from {position} to {pos()}.')
            position = pos()
            time.sleep(60)
            pyautogui.moveRel(0,-50,duration=1)
            position = pos()
            print(f'Moved from {position} to {pos()}.')
            time.sleep(60)
        except KeyboardInterrupt:
            print('Exiting...')
            pyautogui.moveTo(250,250)
            try:
                sys.exit(0)
            except:
                os._exit(0)
print('Starting...')
time.sleep(10)
wiggle()
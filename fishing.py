import pyautogui
import keyboard
import time
import numpy as np
from cv2 import cv2
import mss

THRESHOLD = 60
timePassed = time.time()

def fish():
    pyautogui.click(button='right')
    print('i found a fish!')
    time.sleep(.5)
    pyautogui.click(button='right')
    time.sleep(2)

def measure_time(t1)->bool:
    return time.time() - t1 > 30

print("Press Ctrl-C to stop")
while(1):
    path = ''
    with mss.mss() as sct:
        monitor = {"top": 200, "left": 300, "width": 750, "height": 500}
        output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)
        sct_img = sct.grab(monitor)

        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        path = output
    src = cv2.imread(path)
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

    lower_white = np.array([0, 0, 152])
    upper_white = np.array([180, 79, 255])

    mask = cv2.inRange(hsv, lower_white, upper_white)
    print(cv2.countNonZero(mask))

    if(cv2.countNonZero(mask) < THRESHOLD or measure_time(timePassed)):
        timePassed = time.time()
        fish()


    print("this is the timer: " + str(time.time()))
    print("this is the time passed: " + str(timePassed))
    
    k = cv2.waitKey(5) & 0xFF    
    if k == 27:
        break


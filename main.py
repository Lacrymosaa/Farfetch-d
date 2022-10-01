from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
from win32 import win32api, win32console

time.sleep(3)

def battle():
    pyautogui.press('1')
    time.sleep(np.random.uniform(0.2,0.3))
    pyautogui.press('1')
    time.sleep(0.8)

def walk():
    pyautogui.keyDown('D')
    time.sleep(np.random.uniform(0.6,0.7))
    pyautogui.keyUp('D')
    time.sleep(np.random.uniform(0.1,0.3))
    pyautogui.keyDown('A')
    time.sleep(np.random.uniform(0.6,0.7))
    pyautogui.keyUp('A')

 ### IMPORTANT: Confidence in this line can vary greatly. Just leaving it this way cannot guarantee that it will work.
 ### Another important thing is that Pok1.png not recommended that has no background###
while True:
    walk()
    if pyautogui.locateOnScreen('nickname.png', grayscale=True, confidence=0.5) != None:
        if pyautogui.locateOnScreen('Pok1.png', grayscale=False, confidence=0.38) != None:
            quit()
        time.sleep(1.8)
        battle()

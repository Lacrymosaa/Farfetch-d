from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
from win32 import win32api, win32console

time.sleep(2.5)

def battle():
    pyautogui.press('1')
    time.sleep(np.random.uniform(0.3,0.4))
    pyautogui.press('1')
    time.sleep(0.93)

def walk():
    sametime = np.random.uniform(0.25, 0.40)
    pyautogui.keyDown('D')
    time.sleep(sametime + np.random.uniform(0.01, 0.05))
    pyautogui.keyUp('D')
    time.sleep(np.random.uniform(0.05,0.15)) #Interval of times between keypress
    pyautogui.keyDown('A')
    time.sleep(sametime + np.random.uniform(0.01, 0.05))
    pyautogui.keyUp('A')

 ### IMPORTANT: Confidence in this line can vary greatly. Just leaving it this way cannot guarantee that it will work.
 ### Another important thing is that Pok1.png not recommended that has no background###
while True: #823, 333
    walk()
    if pyautogui.locateOnScreen('nickname.png', grayscale=True, confidence=0.5) != None:
        while pyautogui.locateOnScreen('nickname.png', grayscale=True, confidence=0.5) != None:
            time.sleep(1.95)
            if pyautogui.locateCenterOnScreen('solosis.png', grayscale=True, confidence=0.3, region=(770, 270, 120, 120)) != None:
                print('I FOUND IT!')
                quit()
            battle()
            if pyautogui.locateOnScreen('nickname.png', grayscale=True, confidence=0.5) != None:
                time.sleep(3.5)
                if pyautogui.locateOnScreen('nickname.png', grayscale=True, confidence=0.5) != None:
                    pyautogui.click(x=580 ,y=532)
                    print('I runned.')

### nickname.png is a condition that will show to your program that battle started, but is not possible use moves. 
# In this game i used the nickname bar that shows the battle started



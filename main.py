from pyautogui import *
import pyautogui
import time
import numpy as np



time.sleep(2.5)

def battle():
    pyautogui.press('1')
    time.sleep(np.random.uniform(0.3,0.4))
    pyautogui.press('1')
    time.sleep(0.93)

def walk_D(sametime): 
    pyautogui.keyDown('D')
    time.sleep(sametime)
    pyautogui.keyUp('D')

def walk_A(sametime):
    pyautogui.keyDown('A')
    time.sleep(sametime)
    pyautogui.keyUp('A')

#in pyautogui.pixel(x, y)[] == x the [] number can be 0 (red), 1 (green) or 2 (blue). The x is the third number obtained in where.py
#the number of x,y is a commom point where all pokemon gonna cover

def verify():
    while pyautogui.locateOnScreen('nickname.png', grayscale=True, confidence=0.5) != None:
            time.sleep(1.96)
            if pyautogui.locateCenterOnScreen('mew.png', grayscale=True, confidence=0.18, region=(770, 270, 120, 120)) != None or pyautogui.pixel(825, 335)[2] == 213 or pyautogui.pixel(825, 335)[0] == 238: 
                print('I FOUND IT!')
                quit()
            if pyautogui.locateOnScreen('E.png', grayscale=True, confidence=0.8 ,region=(415, 230, 20, 20)): ###E.png is an exception, a pokemon you cannot OHKO
                pyautogui.click(x=580 ,y=532)
                print('I runned.')
            battle()

 ### IMPORTANT: Confidence in this line can vary greatly. Just leaving it this way cannot guarantee that it will work.
 ### Another important thing is that Pok1.png not recommended that has no background###
while True:
    sametime = np.random.uniform(0.300, 0.400) 
    walk_D(sametime)
    verify()
    walk_A(sametime)
    verify()
    
### nickname.png is a condition that will show to your program that battle started, but is not possible use moves. 
# In this game i used the nickname bar that shows the battle started



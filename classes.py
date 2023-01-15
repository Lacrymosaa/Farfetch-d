from pyautogui import *
import pyautogui
import time
import numpy as np
import os

### WALK PART
def walk(pause): 
    pyautogui.keyDown('D')
    time.sleep(pause)
    pyautogui.keyUp('D')
    pyautogui.keyDown('A')
    time.sleep(pause)
    pyautogui.keyUp('A')
   
### END WALK PART
def chat():
    if pyautogui.locateOnScreen('name.png', grayscale=True, confidence=0.698, region=(988, 595, 340, 180)):
        print('I caught the name of pokemon!')
        os.startfile('alarm.mp3')
        quit()

# Try to check de pokemon in screen (this part always fail miserable)

def check():
    if pyautogui.locateCenterOnScreen('moltres.png', grayscale=True, confidence=0.32, region=(770, 270, 120, 120)) != None: 
        time.sleep(1.5)
        if pyautogui.locateOnScreen('nickname.png', grayscale=True, confidence=0.5) != None:
            print('I found Moltres!')
            os.startfile('alarm.mp3')
            quit()

def elite():    ###E.png is an exception, a pokemon you cannot OHKO
    while pyautogui.locateOnScreen('E.png', grayscale=True, confidence=0.65 ,region=(415, 230, 20, 20)): 
        if pyautogui.locateOnScreen('fight_button.png', grayscale=True, confidence=0.8) != None:
            pyautogui.press('4')
            return True
    else:
        return False

### Battle part, for my purposes it can be used like that
def battle():
    while pyautogui.locateOnScreen('nickname.png', grayscale=True, confidence=0.5) != None:
        if pyautogui.locateOnScreen('fight_button.png', grayscale=True, confidence=0.8) != None:
            pyautogui.press('1')
            time.sleep(np.random.uniform(0.35,0.4))
            pyautogui.press('1', presses= 2)
            time.sleep(0.2)

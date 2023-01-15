import pyautogui
import time
import numpy as np
from classes import *

time.sleep(1)

# Def run is used for run of pokemon you cannot kill
def run():
    if pyautogui.locateCenterOnScreen('run.png', grayscale=True, confidence=0.36, region=(770, 270, 140, 140)) != None or pyautogui.locateCenterOnScreen('liepard.png', grayscale=True, confidence=0.4, region=(770, 270, 120, 120)) != None:
        while pyautogui.locateOnScreen('nickname.png', grayscale=True, confidence=0.5) != None:
            if pyautogui.locateOnScreen('fight_button.png', grayscale=True, confidence=0.8) != None:
                pyautogui.click('coordinates of click')
                return True

# Verify is used for check if you are in battle or not
# Chat is a condition to check if you found the pokemon you wanty
# The second image is the image of battle button for the program execute the battle process just when its needed
def verify():
    if pyautogui.locateOnScreen('battlestartconfirmation.png', grayscale=True, confidence=0.5) != None:
        chat()
        if pyautogui.locateOnScreen('buttonofbattle.png', grayscale=True, confidence=0.8) != None:
            chat()
            battle()

# the second while is just while you are not in battle, walking to left and right in the same period
# verify is the definition bellow
while True:
    while pyautogui.locateOnScreen('battlestartconfirmation.png', grayscale=True, confidence=0.5) == None:
        sametime = np.random.uniform(0.400, 0.500) 
        walk(sametime)
    verify()

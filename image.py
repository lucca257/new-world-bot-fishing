from pyautogui import * 
import pyautogui 
import keyboard
import time

#CONSTANT
region=(1154,64,226,794)

while keyboard.is_pressed('q') == False :
    if pyautogui.locateOnScreen('images/waiting_for_fish.jpg',region=region,confidence=0.8) != None:
        print("waiting for a fish ...")
        time.sleep(0.2)
    
    if pyautogui.locateOnScreen('images/fish_noticed.jpg',region=region,confidence=0.8) != None:
        print("*** fish noticed ***")
        time.sleep(0.3)
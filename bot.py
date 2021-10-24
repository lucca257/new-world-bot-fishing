from pyautogui import * 
import pyautogui 
import time
import keyboard
import win32api, win32con
import actions

#CONSTANT
region=(1154,64,226,794)
reelingColor = (4, 227, 162)
warningColor = (230, 110, 22)
pauseColor = (109, 18, 21)
img = pyautogui.screenshot(region=region)

def pixel_match(color, matcher):
    for i in range (0,3):
        if not((matcher[i] - 7) <= color[i] <= (matcher[i] + 7)):
            return False
    return True

def color_recognition():
    img = pyautogui.screenshot(region=region)
    colorStatus = 0

    for x in range(img.width):    
        for y in range(img.height):
            color = img.getpixel((x, y))

            if pixel_match(color, reelingColor):
                colorStatus = 1
                break

            elif pixel_match(color, warningColor):
                colorStatus = 2
                break

            elif pixel_match(color, pauseColor):
                colorStatus = 3
                break    

    return colorStatus    

def image_recognition():
    if pyautogui.locateOnScreen('images/waiting_for_fish.png',region=region,confidence=0.8) != None:
        return 1
    
    if pyautogui.locateOnScreen('images/fish_noticed.png',region=region,confidence=0.8) != None:
        return 2
    
    return 0

def verifyEndTime(timeout_start, timeout):
    if (time.time() < timeout_start + timeout):
        return True
    return False

while keyboard.is_pressed('q') == False :
    status = image_recognition()
    
    if status == 0 :
        actions.reelFish()
    if status == 1 :
        print("waiting for a fish ...")
    if status == 2 :
        actions.fishNoticed()
        loop = True
        timeout = 5
        timeout_start = time.time()        

        while loop:
            colorStatus = color_recognition()
            if not verifyEndTime(timeout_start, timeout):
                print("*** FISH CAUGHT ***")
                loop = False
                break

            if colorStatus != 0:
                timeout_start = time.time()    
            if colorStatus == 1 :
                actions.castFish()
            if colorStatus == 2 :
                actions.rest()
            if colorStatus == 3 :
                actions.pause()
from pyautogui import * 
import pyautogui 
import time
import keyboard
import actions

#CONSTANT
region=(1154,64,226,794)
reelingColor = (4, 227, 162)
warningColor = (230, 110, 22)
pauseColor = (109, 18, 21)
img = pyautogui.screenshot(region=region)
repairTimout = 400
repairTimoutStart = time.time()

def pixel_match(color, matcher):
    for i in range (0,3):
        if not((matcher[i] - 7) <= color[i] <= (matcher[i] + 7)):
            return False
    return True

def color_recognition():
    img = pyautogui.screenshot(region=region)
    for x in range(img.width):
        for y in range(img.height):
            color = img.getpixel((x, y))
            if pixel_match(color, reelingColor):
                return 1
            elif pixel_match(color, warningColor):
                return 2
            elif pixel_match(color, pauseColor):
                return 3
    return 0

def image_recognition():
    if pyautogui.locateOnScreen('images/waiting_for_fish.png',region=region,confidence=0.7) != None:
        return 1
    if pyautogui.locateOnScreen('images/fish_noticed.png',region=region,confidence=0.7) != None:
        return 2
    return 0

def verifyEndTime(timeout_start, timeout):
    return time.time() > timeout_start + timeout

actions.startWithFishRod()

while keyboard.is_pressed('q') == False :
    status = image_recognition()
    if status == 0 and verifyEndTime(repairTimoutStart, repairTimout):
        actions.repairFishRod()
        time.sleep(1)
        actions.moviment()
        repairTimoutStart = time.time()  
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
            if verifyEndTime(timeout_start, timeout):
                print("*** FISH CAUGHT ***")
                time.sleep(4)
                actions.releaseVisionPosition()
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
print("exit bot")
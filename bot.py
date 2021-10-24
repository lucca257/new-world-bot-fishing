from pyautogui import * 
import pyautogui 
import time
import keyboard

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
                #time.sleep(1)
                break

            elif pixel_match(color, warningColor):
                colorStatus = 2
                #time.sleep(2)
                break

            elif pixel_match(color, pauseColor):
                colorStatus = 3
                #time.sleep(3)
                break    

    return colorStatus    

def image_recognition():
    if pyautogui.locateOnScreen('images/waiting_for_fish.png',region=region,confidence=0.8) != None:
        time.sleep(0.2)
        return 1
    
    if pyautogui.locateOnScreen('images/fish_noticed.png',region=region,confidence=0.8) != None:
        time.sleep(0.3)
        return 2
    
    return 0

while keyboard.is_pressed('q') == False :
    status = image_recognition()

    if status == 0 :
        print("image not founded yet")
    if status == 1 :
        print("waiting for a fish ...")
    if status == 2 :
        print("*** fish noticed ***")

        loop = True
        timeout = 5
        timeout_start = time.time()

        print("start loop")

        while loop:
            colorStatus = color_recognition()

            if not (time.time() < timeout_start + timeout):
                print("*** Loop Reset ***")
                loop = False
                break

            if colorStatus != 0:
                timeout_start = time.time()    
            if colorStatus == 0 :
                print("nothing")
            if colorStatus == 1 :
                print("green ...")
            if colorStatus == 2 :
                print("warning color ...")
            if colorStatus == 3 :
                print("pause reling ...")

        print("end loop")
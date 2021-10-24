from pyautogui import * 
import pyautogui 
import time
import keyboard

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

def find_color():
    img = pyautogui.screenshot(region=region)
    colorFound = False
    for x in range(img.width):    
        for y in range(img.height):
            color = img.getpixel((x, y))

            if pixel_match(color, reelingColor):
                print("green ...")
                colorFound = True
                #time.sleep(1)
                break

            elif pixel_match(color, warningColor):
                print("warning color ...")
                colorFound = True
                time.sleep(1)
                break

            elif pixel_match(color, pauseColor):
                print("pause reling ...")
                colorFound = True
                time.sleep(2)
                break    

    return colorFound

while keyboard.is_pressed('q') == False :
    color = find_color()
    if not color:
        print("color not found") 
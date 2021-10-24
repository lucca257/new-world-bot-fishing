import mouseKeyboard
import time

def reelFish():
    print("reeling fish ...")
    mouseKeyboard.startClickMouse()
    time.sleep(0.9)
    mouseKeyboard.stopClickMouse()
    time.sleep(2.5)

def fishNoticed():
    print("*** fish noticed ***")
    mouseKeyboard.startClickMouse()
    time.sleep(0.3)
    mouseKeyboard.stopClickMouse()

def castFish():
    print("green color, casting fish...")
    mouseKeyboard.startClickMouse()

def rest():
    print("warning, resting ...")
    mouseKeyboard.stopClickMouse()
    time.sleep(0.5)

def pause():
    print("danger, stop ...")
    mouseKeyboard.stopClickMouse()
    time.sleep(1.2)
    
def repairFishRod():
    print("*** reparing fish rod ***")
    time.sleep(5)
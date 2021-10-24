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
    time.sleep(3)
    print("*** reparing fish rod ***")
    
    print("Open inventory")
    openIventory()
    
    print("Trying repair")
    mouseKeyboard.clickMouseCordenates(1129,660)
    time.sleep(0.2)
    mouseKeyboard.pressKey(0x52)
    time.sleep(0.2)
    mouseKeyboard.startClickMouse()
    time.sleep(0.2)
    mouseKeyboard.stopClickMouse()
    time.sleep(0.2)
    
    print("Confirm repair")
    mouseKeyboard.pressKey(0x45)
    time.sleep(0.2)
    
    print("Close inventory")
    openIventory()
    time.sleep(1)
    
    print("Switch to fish rod")
    switchFishRod()

def openIventory():
    mouseKeyboard.pressReleaseKey(0x09)
def switchFishRod():
    mouseKeyboard.pressReleaseKey(0x72)
    
def startWithFishRod():
    openIventory()
    time.sleep(0.1)
    openIventory()
    time.sleep(1)
    switchFishRod()
    time.sleep(0.1)
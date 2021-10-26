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
    pressVisionPosition()

def castFish():
    print("green color, casting fish...")
    mouseKeyboard.startClickMouse()

def rest():
    print("warning, resting ...")
    mouseKeyboard.stopClickMouse()
    time.sleep(0.8)

def pause():
    print("danger, stop ...")
    mouseKeyboard.stopClickMouse()
    time.sleep(1.2)
    
def repairFishRod():
    print("*** reparing fish rod ***")
    
    print("Open inventory")
    openIventory()
    
    print("Trying repair")
    mouseKeyboard.clickMouseCordenates(1129,660)
    time.sleep(0.2)
    mouseKeyboard.pressKey(0x52)
    time.sleep(0.2)
    mouseKeyboard.startClickMouse()
    time.sleep(0.5)
    mouseKeyboard.stopClickMouse()
    time.sleep(0.5)
    
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
    time.sleep(0.5)
    openIventory()
    time.sleep(1)
    switchFishRod()
    time.sleep(0.1)
    
def pressVisionPosition():
    mouseKeyboard.pressKey(0x42)
    time.sleep(0.1)

def releaseVisionPosition():
    mouseKeyboard.releaseKey(0x42)
    time.sleep(0.1)

def moviment():
    print("moving the legs ...")
    mouseKeyboard.pressReleaseKey(0x20)
    time.sleep(0.3)
    mouseKeyboard.pressReleaseKey(0x41)
    time.sleep(0.3)
    mouseKeyboard.pressReleaseKey(0x44)
    mouseKeyboard.pressReleaseKey(0x41)
    mouseKeyboard.pressReleaseKey(0x41)
    mouseKeyboard.pressReleaseKey(0x41)
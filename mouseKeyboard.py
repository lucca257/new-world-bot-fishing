import win32api, win32con
import time

def clickMouseCordenates(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.3)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def startClickMouse():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)

def stopClickMouse():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
 
def pressReleaseKey(key):
    pressKey(key)
    releaseKey(key)
    
def pressKey(key):
    win32api.keybd_event(key,0,0,0)
    time.sleep(0.1)

def releaseKey(key):
    win32api.keybd_event(key,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(0.1)
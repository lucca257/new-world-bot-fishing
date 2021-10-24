import win32api, win32con
import time

def clickMouseCordenates(x,y):
    win32api.SetCursorPos((x,y))
    time.sleep(0.3)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.3)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def startClickMouse():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)

def stopClickMouse():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
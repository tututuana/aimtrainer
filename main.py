import pyautogui
from time import sleep
import win32api, win32con
import keyboard

sleep(3)
def click(x,y):
    win32api.SetCursorPos((x,y))
    sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while True:
    if keyboard.is_pressed('q'):
        break
    pic = pyautogui.screenshot(region=(573, 301, 804, 482))
    width, height = pic.size

    for x in range(0, width, 5):
        for y in range(0, height, 5):
            r, g, b = pic.getpixel((x, y))
            if b == 34 and r == 255 and g == 87:
                click(x+573, y+301)
                sleep(0.04)
                break
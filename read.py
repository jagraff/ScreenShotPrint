try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

import sys
import os
import datetime

import glob

def print_image(filename):
    print(filename)
    print(pytesseract.image_to_string(Image.open(filename)))

def get_latest_screenshot():
    screenshot_files = sorted(glob.glob('Screen Shot *'), key=lambda d: datetime.datetime.strptime(d, "Screen Shot %Y-%m-%d at %I.%M.%S %p.png"), reverse=True)

    return screenshot_files[0]

curr_path = os.getcwd()
desktop_path = os.path.join(os.environ["HOME"], "Desktop")
os.chdir(desktop_path)
print_image(get_latest_screenshot())
os.chdir(curr_path)

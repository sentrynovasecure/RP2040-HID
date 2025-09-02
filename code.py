import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from lib.keyboard_layout_win_fr import KeyboardLayout
import adafruit_ducky

time.sleep(2.5)  # let the OS detect the keyboard

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayout(keyboard)

duck = adafruit_ducky.Ducky("payload.txt", keyboard, layout)

while duck.loop():
    pass
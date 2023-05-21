#-*- coding: utf-8 -*-#

# For interfacing with 0.9" OLED display (128x32) over I2C.

# To prepare:
# sudo apt-get install python3-pip
# sudo pip3 install adafruit-circuitpython-ssd1306
# sudo apt-get install python3-pil
#
# enable I2C in `raspi-config`
# verify that the I2C device is visible with `i2cdetect -y 1`

# SPDX-FileCopyrightText: 2017 Tony DiCola for Adafruit Industries
# SPDX-FileCopyrightText: 2017 James DeVito for Adafruit Industries
# SPDX-License-Identifier: MIT

# This example is for use on (Linux) computers that are using CPython with
# Adafruit Blinka to support CircuitPython libraries. CircuitPython does
# not support PIL/pillow (python imaging library)!

import sys
import time
import subprocess

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306


fileName = sys.argv[1]

# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Clear display.
disp.fill(0)
disp.show()

width = disp.width
height = disp.height

image = Image.open(fileName).convert('1') #.convert(mode='1',dither=Image.FLOYDSTEINBERG)

disp.image(image)
disp.show()

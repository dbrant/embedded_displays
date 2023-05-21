#-*- coding: utf-8 -*-#

# For interfacing with 1.3" OLED display (128x64) over SPI.
# https://www.aliexpress.com/item/32960473206.html

# Code adapted from:
# https://github.com/8TN/Raspberry-Pi-SH1106-oled-display

# 4 wire SPI interface
#  RASPBERRY PI GPIO >>> SH1106 1.3 inch display
# 3.3v P1-17 3.3v    ->- VCC
# RES  P1-18 GPIO-24 ->- RES (reset)
# MOSI P1-19 GPIO-10 ->- MOSI
# A0   P1-22 GPIO-25 ->- DC (data/command)
# SCLK P1-23 GPIO-11 ->- CLK
# CE0  P1-24 GPIO-08 ->- CS (chip select)
# GND  P1-25 GND     ->- GND

import spidev, time, sys
import RPi.GPIO as GPIO
from PIL import Image

#initialisation des GPIO
GPIO.setmode(GPIO.BOARD)
A0 = 22 #GPIO pin for A0 pin : 0 -> command; 1 -> display data RAM
RESN = 18 #GPIO pin for display reset (active low)
GPIO.setup(A0, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(RESN, GPIO.OUT, initial=GPIO.HIGH)

spi = spidev.SpiDev()
spi.open(0, 0) #bus = 0 , device = 0
spi.max_speed_hz = 1000000
spi.mode = 0b00
#spi.bits_per_word = 8

def display_img(image):
    data_slice=[[],[],[],[],[],[],[],[]]
    GPIO.output(A0, 0)
    for p in range (0,8):
        data_set = []
        for c in range (0,128):
            by = 0x00
            for b in range (0,8):
                by = by>>1 | (image.getpixel((c, p*8+b))& 0x80)
            data_set.append(by)
        data_slice[p]=data_set
    spi.xfer([0xAF])
    for p in range (0,8):
        GPIO.output(A0, 0)
        spi.xfer([0xB0+p, 0x02, 0x10])
        GPIO.output(A0, 1)
        spi.xfer(data_slice[p])

GPIO.output(RESN, 0)
time.sleep(0.1)
GPIO.output(RESN, 1)
time.sleep(0.1)

try:
    file = "bissel4.bmp"
    while True:
        img = Image.open(file).convert('1') #.convert(mode='1',dither=Image.FLOYDSTEINBERG)
        display_img(img)
        file = raw_input("filename: ")

except KeyboardInterrupt:
    disp.module_exit()
    exit()
except:
    print("Error: ", sys.exc_info())

spi.close()
GPIO.cleanup()


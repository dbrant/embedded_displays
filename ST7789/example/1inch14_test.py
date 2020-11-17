#!/usr/bin/python
# -*- coding: UTF-8 -*-

# For interfacing with 1.14" color TFT display (240x135) over SPI.
# https://www.aliexpress.com/item/32983040121.html
#
# Adapted from default Waveshare example code.
#
# Pin connections to Raspberry Pi:
# VCC -> 3.3V
# GND -> GND
# SCL -> SCLK (23, BCM 11)
# SDA -> MOSI (19, BCM 10)
# RES -> 13 (BCM 27)
# DC -> 22 (BCM 25)
# CS -> CE0 (24, BCM 8)
# BLK -> optional (backlight: default on; connect to ground to turn off)

import os
import sys
import time
import logging
import spidev as SPI
sys.path.append("..")
from lib import LCD_1inch14
from PIL import Image,ImageDraw,ImageFont

# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 18
bus = 0
device = 0
logging.basicConfig(level=logging.DEBUG)
try:
    # display with hardware SPI:
    #disp = LCD_1inch14.LCD_1inch14(spi=SPI.SpiDev(bus, device),spi_freq=10000000,rst=RST,dc=DC,bl=BL)
    disp = LCD_1inch14.LCD_1inch14()
    # Initialize library.
    disp.Init()
    #disp.clear()

    image = Image.open('bissel2.png')
    disp.ShowImage(image)

    disp.module_exit()
except IOError as e:
    logging.info(e)
except KeyboardInterrupt:
    disp.module_exit()
    exit()

from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
#import sh1107

import max6675
import framebuf
from time import sleep


# Dual thermocouples, with a small OLED display.
# Intended to run on my ESP32-C3 dev board.


#led = Pin(8, Pin.OUT)
#led.value(1)

tc1 = max6675.MAX6675(Pin(0,Pin.OUT),Pin(1,Pin.OUT),Pin(2,Pin.IN))
tc2 = max6675.MAX6675(Pin(10,Pin.OUT),Pin(9,Pin.OUT),Pin(8,Pin.IN))

oled = SSD1306_I2C(128,64,SoftI2C(scl=Pin(21),sda=Pin(20),freq=200000))

#oled = sh1107.SH1107_I2C(128, 128, SoftI2C(scl=Pin(21), sda=Pin(20), freq=400000), address=0x3c, rotate=90)
oled.contrast(0xff)

while True:
    temp1 = tc1.read()
    temp2 = tc2.read()
    oled.fill(0)
    oled.text("1: " + str(temp1), 0, 16)
    oled.text("2: " + str(temp2), 0, 36)
    oled.show()
    sleep(0.25)

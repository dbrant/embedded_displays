from machine import Pin, SoftI2C
from lcd2004 import LCD
from time import sleep

# If the backlight turns on, but you don't see any text,
# don't forget to adjust the contrast trim pot!

scl_pin = 28
sda_pin = 29
lcd = LCD(SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin), freq=100000))
lcd.puts("YES!")

led = Pin(17, Pin.OUT)

while True:
  led.value(1)
  sleep(0.5)
  led.value(0)
  sleep(0.5)

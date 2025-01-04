#include <U8g2lib.h>
#include <Wire.h>

// NOTE: This is intended to work with my ESP32-C3 dev board that has a tiny onboard display.

#define PIN_LED 8

// there is no 72x40 constructor in u8g2 library that works with this screen as of 13.09.2024,
// hence the 72x40 screen is mapped in the middle of the 132x64 pixel buffer of the SSD1306 controller
U8G2_SSD1306_128X64_NONAME_F_HW_I2C u8g2(U8G2_R0, U8X8_PIN_NONE, 6, 5); // rotation, reset, SDA, SCL
int width = 72;
int height = 40;
int xOffset = 30; // = (132-w)/2
int yOffset = 12; // = (64-h)/2

void setup(void) {
  pinMode(PIN_LED, OUTPUT);
  
  u8g2.begin();
  u8g2.setContrast(255); // set contrast to maximum
  u8g2.setBusClock(400000); //400kHz I2C
  u8g2.setFont(u8g2_font_pxplusibmcga_8f); //u8g2_font_ncenB10_tr);

  u8g2.clearBuffer(); // clear the internal memory
  u8g2.drawFrame(xOffset+0, yOffset+0, width, height); //draw a frame around the border
  u8g2.setCursor(xOffset+5, yOffset+25);
  u8g2.printf("YES!");
  u8g2.sendBuffer(); // transfer internal memory to the display
}

void loop(void) {
  int i;
  for (i = 0; i < 5; i++) {
    digitalWrite(PIN_LED, HIGH);  // turn the LED on (HIGH is the voltage level)
    delay(200);                      // wait for a second
    digitalWrite(PIN_LED, LOW);   // turn the LED off by making the voltage LOW
    delay(200);
  }
}

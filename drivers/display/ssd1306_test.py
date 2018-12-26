from machine import I2C
i2c=machine.I2C(-1, sda=machine.Pin("PB9"), scl=machine.Pin("PB8"), freq=400000)  

from ssd1306 import SSD1306_I2C
oled = SSD1306_I2C(128, 64, i2c)
oled.text("Hello PYB Nano", 0, 0)
oled.show()
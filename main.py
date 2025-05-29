'''
Основной файл терпинала.
Запускать его.
'''

from machine import *
from ssd1306 import SSD1306_I2C
from utime import *
from keyboard import *
from playsong import *
from handler import *
import sys

#переменные
i2c = I2C(0 ,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

#вступление
oled.text("help - B,", 0, 0)
oled.text("enter - *", 0, 10)
oled.show()
i += 20

#цикл
prog = ''
while True:
    key = keypadRead()
    if key == 'enter':
        code = prog
        prog = ''
        run(oled, melody, playsong, code)
    elif key != -1:
        prog += str(key)
        oled.text(key, j, i)
        oled.show()
        j += len(str(key)) * 10

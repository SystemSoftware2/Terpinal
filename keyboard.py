'''
Файл для "драйвера" клавиатуры.
Именно здесь программа понимает название клавиши.
A - clear
B - help
C - music
D - history
# - exit
* - enter
Ну и цифры.
'''
from machine import *

#Обозначение клавиш
keyName = [['1', '2', '3', 'clear'],
           ['4', '5', '6', 'help'],
           ['7', '8', '9', 'music'],
           ['enter', '0', 'exit', 'history']]
keypadRowPins = [13, 12, 11, 10]
keypadColPins = [9, 8, 7, 6]

#Их добавление
row = []
col = []
keypadState = []
for i in keypadRowPins:
    row.append(Pin(i, Pin.IN, Pin.PULL_UP))
    keypadState.append([0, 0, 0, 0])
for i in keypadColPins:
    col.append(Pin(i, Pin.OUT))

#Чтение нажатой клавишы
def keypadRead():
    '''
    Возращает:
    -1 если не нажато.
    Название клавишы.
    '''
  
    j_ifPressed = -1
    i_ifPressed = -1
  
    for i in range(len(col)):
        col[i].low()
        sleep(0.005)
        for j in range(len(row)):
            pressed = not row[j].value()
            if pressed and not keypadState[j][i]:
                keypadState[j][i] = pressed
            elif not pressed and keypadState[j][i]:
                keypadState[j][i] = pressed
                j_ifPressed = j
                i_ifPressed = i
        col[i].high()
      
    if j_ifPressed != -1 and i_ifPressed != -1:
        return keyName[j_ifPressed][i_ifPressed]
    else:
        return -1

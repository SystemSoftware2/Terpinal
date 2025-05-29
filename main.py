from machine import *
from ssd1306 import SSD1306_I2C
from utime import *
import sys

notesforboot = {
"NOTE_B0": 31,
"NOTE_C1": 33,
"NOTE_CS1": 35,
"NOTE_D1": 37,
"NOTE_DS1": 39,
"NOTE_E1": 41,
"NOTE_F1": 44,
"NOTE_FS1": 46,
"NOTE_G1": 49,
"NOTE_GS1": 52,
"NOTE_A1": 55,
"NOTE_AS1": 58,
"NOTE_B1": 62,
"NOTE_C2": 65,
"NOTE_CS2": 69,
"NOTE_D2": 73,
"NOTE_DS2": 78,
"NOTE_E2": 82,
"NOTE_F2": 87,
"NOTE_FS2": 93,
"NOTE_G2": 98,
"NOTE_GS2": 104,
"NOTE_A2": 110,
"NOTE_AS2": 117,
"NOTE_B2": 123,
"NOTE_C3": 131,
"NOTE_CS3": 139,
"NOTE_D3": 147,
"NOTE_DS3": 156,
"NOTE_E3": 165,
"NOTE_F3": 175,
"NOTE_FS3": 185,
"NOTE_G3": 196,
"NOTE_GS3": 208,
"NOTE_A3": 220,
"NOTE_AS3": 233,
"NOTE_B3": 247,
"NOTE_C4": 262,
"NOTE_CS4": 277,
"NOTE_D4": 294,
"NOTE_DS4": 311,
"NOTE_E4": 330,
"NOTE_F4": 349,
"NOTE_FS4": 370,
"NOTE_G4": 392,
"NOTE_GS4": 415,
"NOTE_A4": 440,
"NOTE_AS4": 466,
"NOTE_B4": 494,
"NOTE_C5": 523,
"NOTE_CS5": 554,
"NOTE_D5": 587,
"NOTE_DS5": 622,
"NOTE_E5": 659,
"NOTE_F5": 698,
"NOTE_FS5": 740,
"NOTE_G5": 784,
"NOTE_GS5": 831,
"NOTE_A5": 880,
"NOTE_AS5": 932,
"NOTE_B5": 988,
"NOTE_C6": 1047,
"NOTE_CS6": 1109,
"NOTE_D6": 1175,
"NOTE_DS6": 1245,
"NOTE_E6": 1319,
"NOTE_F6": 1397,
"NOTE_FS6": 1480,
"NOTE_G6": 1568,
"NOTE_GS6": 1661,
"NOTE_A6": 1760,
"NOTE_AS6": 1865,
"NOTE_B6": 1976,
"NOTE_C7": 2093,
"NOTE_CS7": 2217,
"NOTE_D7": 2349,
"NOTE_DS7": 2489,
"NOTE_E7": 2637,
"NOTE_F7": 2794,
"NOTE_FS7": 2960,
"NOTE_G7": 3136,
"NOTE_GS7": 3322,
"NOTE_A7": 3520,
"NOTE_AS7": 3729,
"NOTE_B7": 3951,
"NOTE_C8": 4186,
"NOTE_CS8": 4435,
"NOTE_D8": 4699,
"NOTE_DS8": 4978
}

melody = []

notes = ['Nokia Ringtone', 180, 'NOTE_E5', '8', 'NOTE_D5', '8', 'NOTE_FS4', '4', 'NOTE_GS4', '4', 'NOTE_CS5', '8', 'NOTE_B4', '8', 'NOTE_D4', '4', 'NOTE_E4', '4', 'NOTE_B4', '8', 'NOTE_A4', '8', 'NOTE_CS4', '4', 'NOTE_E4', '4', 'NOTE_A4', '2']
melody.append(notes)

notes = ['Take on me - A-ha', 140, 'NOTE_FS5', '8', 'NOTE_FS5', '8', 'NOTE_D5', '8', 'NOTE_B4', '8', 'REST', '8', 'NOTE_B4', '8', 'REST', '8', 'NOTE_E5', '8', 'REST', '8', 'NOTE_E5', '8', 'REST', '8', 'NOTE_E5', '8', 'NOTE_GS5', '8', 'NOTE_GS5', '8', 'NOTE_A5', '8', 'NOTE_B5', '8', 'NOTE_A5', '8', 'NOTE_A5', '8', 'NOTE_A5', '8', 'NOTE_E5', '8', 'REST', '8', 'NOTE_D5', '8', 'REST', '8', 'NOTE_FS5', '8', 'REST', '8', 'NOTE_FS5', '8', 'REST', '8', 'NOTE_FS5', '8', 'NOTE_E5', '8', 'NOTE_E5', '8', 'NOTE_FS5', '8', 'NOTE_E5', '8', 'NOTE_FS5', '8', 'NOTE_FS5', '8', 'NOTE_D5', '8', 'NOTE_B4', '8', 'REST', '8', 'NOTE_B4', '8', 'REST', '8', 'NOTE_E5', '8', 'REST', '8', 'NOTE_E5', '8', 'REST', '8', 'NOTE_E5', '8', 'NOTE_GS5', '8', 'NOTE_GS5', '8', 'NOTE_A5', '8', 'NOTE_B5', '8', 'NOTE_A5', '8', 'NOTE_A5', '8', 'NOTE_A5', '8', 'NOTE_E5', '8', 'REST', '8', 'NOTE_D5', '8', 'REST', '8', 'NOTE_FS5', '8', 'REST', '8', 'NOTE_FS5', '8', 'REST', '8', 'NOTE_FS5', '8', 'NOTE_E5', '8', 'NOTE_E5', '8', 'NOTE_FS5', '8', 'NOTE_E5', '8', 'NOTE_FS5', '8', 'NOTE_FS5', '8', 'NOTE_D5', '8', 'NOTE_B4', '8', 'REST', '8', 'NOTE_B4', '8', 'REST', '8', 'NOTE_E5', '8', 'REST', '8', 'NOTE_E5', '8', 'REST', '8', 'NOTE_E5', '8', 'NOTE_GS5', '8', 'NOTE_GS5', '8', 'NOTE_A5', '8', 'NOTE_B5', '8', 'NOTE_A5', '8', 'NOTE_A5', '8', 'NOTE_A5', '8', 'NOTE_E5', '8', 'REST', '8', 'NOTE_D5', '8', 'REST', '8', 'NOTE_FS5', '8', 'REST', '8', 'NOTE_FS5', '8', 'REST', '8', 'NOTE_FS5', '8', 'NOTE_E5', '8', 'NOTE_E5', '8', 'NOTE_FS5', '8', 'NOTE_E5', '8']
melody.append(notes)

notes = ['Star Wars theme', 108, 'NOTE_AS4', '8', 'NOTE_AS4', '8', 'NOTE_AS4', '8', 'NOTE_F5', '2', 'NOTE_C6', '2', 'NOTE_AS5', '8', 'NOTE_A5', '8', 'NOTE_G5', '8', 'NOTE_F6', '2', 'NOTE_C6', '4', 'NOTE_AS5', '8', 'NOTE_A5', '8', 'NOTE_G5', '8', 'NOTE_F6', '2', 'NOTE_C6', '4', 'NOTE_AS5', '8', 'NOTE_A5', '8', 'NOTE_AS5', '8', 'NOTE_G5', '2', 'NOTE_C5', '8', 'NOTE_C5', '8', 'NOTE_C5', '8', 'NOTE_F5', '2', 'NOTE_C6', '2', 'NOTE_AS5', '8', 'NOTE_A5', '8', 'NOTE_G5', '8', 'NOTE_F6', '2', 'NOTE_C6', '4', 'NOTE_AS5', '8', 'NOTE_A5', '8', 'NOTE_G5', '8', 'NOTE_F6', '2', 'NOTE_C6', '4', 'NOTE_AS5', '8', 'NOTE_A5', '8', 'NOTE_AS5', '8', 'NOTE_G5', '2', 'NOTE_C5', '-8', 'NOTE_C5', '16', 'NOTE_D5', '-4', 'NOTE_D5', '8', 'NOTE_AS5', '8', 'NOTE_A5', '8', 'NOTE_G5', '8', 'NOTE_F5', '8', 'NOTE_F5', '8', 'NOTE_G5', '8', 'NOTE_A5', '8', 'NOTE_G5', '4', 'NOTE_D5', '8', 'NOTE_E5', '4', 'NOTE_C5', '-8', 'NOTE_C5', '16', 'NOTE_D5', '-4', 'NOTE_D5', '8', 'NOTE_AS5', '8', 'NOTE_A5', '8', 'NOTE_G5', '8', 'NOTE_F5', '8', 'NOTE_C6', '-8', 'NOTE_G5', '16', 'NOTE_G5', '2', 'REST', '8', 'NOTE_C5', '8', 'NOTE_D5', '-4', 'NOTE_D5', '8', 'NOTE_AS5', '8', 'NOTE_A5', '8', 'NOTE_G5', '8', 'NOTE_F5', '8', 'NOTE_F5', '8', 'NOTE_G5', '8', 'NOTE_A5', '8', 'NOTE_G5', '4', 'NOTE_D5', '8', 'NOTE_E5', '4', 'NOTE_C6', '-8', 'NOTE_C6', '16', 'NOTE_F6', '4', 'NOTE_DS6', '8', 'NOTE_CS6', '4', 'NOTE_C6', '8', 'NOTE_AS5', '4', 'NOTE_GS5', '8', 'NOTE_G5', '4', 'NOTE_F5', '8', 'NOTE_C6', '1']
melody.append(notes)

buzzer = PWM(Pin(2))   # pin where buzzer is connected

volume = 600   # set volume to a value between 0 and 1000

# functions to play the melodies

def playtone(frequency):
    buzzer.duty_u16(volume)
    buzzer.freq(frequency)

def be_quiet():
    buzzer.duty_u16(0)  # turns sound off

def duration(tempo, t):
    
    # calculate the duration of a whole note in milliseconds (60s/tempo)*4 beats
    wholenote = (60000 / tempo) * 4
    
    # calculate the duration of the current note
    # (we need an integer without decimals, hence the // instead of /)
    if t > 0:
      noteDuration = wholenote // t
    elif (t < 0):
      # dotted notes are represented with negative durations
      noteDuration = wholenote // abs(t)
      noteDuration *= 1.5 # increase their duration by a half
    
    return noteDuration

def playsong(mysong):
    try:
        tempo = mysong[1] # get the tempo for this song from the melodies list 

        # iterate over the notes of the melody. 
        # The array is twice the number of notes (notes + durations)
        for thisNote in range(2, len(mysong), 2):
            
            noteduration = duration(tempo, int(mysong[thisNote+1]))
            
            if (mysong[thisNote] == "REST"):
                be_quiet()
            else:
                playtone(notesforboot[mysong[thisNote]])
            
            sleep(noteduration*0.9/1000) # we only play the note for 90% of the duration...
            be_quiet()
            sleep(noteduration*0.1/1000) # ... and leave 10% as a pause between notes
            
    except: # make sure the buzzer stops making noise when something goes wrong or when the script is stopped
        be_quiet()
        

playsong(["Boot sound", 90, "NOTE_E5", 9, "NOTE_D5", 13, 'NOTE_FS5', '10', 'NOTE_FS5', '13', 'NOTE_D5', '3', 'NOTE_C5', '13', 'NOTE_F5', '5', 'NOTE_C6', '6'])

class TerpinalError(Exception):
    pass

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)
                
history = []

keyName = [['1', '2', '3', 'clear'],
           ['4', '5', '6', 'help'],
           ['7', '8', '9', 'music'],
           ['enter', '0', 'exit', 'history']]
keypadRowPins = [13, 12, 11, 10]
keypadColPins = [9, 8, 7, 6]

row = []
col = []
keypadState = []
for i in keypadRowPins:
    row.append(Pin(i, Pin.IN, Pin.PULL_UP))
    keypadState.append([0, 0, 0, 0])
for i in keypadColPins:
    col.append(Pin(i, Pin.OUT))

def keypadRead():
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
    
i = 0
j = 0
    
def run(com):
    global i, j, history
    
    if com == 'clear':
        oled.fill(0)
        oled.show()
        i = 0
        j = 0
    elif com == 'exit':
        oled.fill(0)
        oled.show()
        oled.text("Goodbay!", 35, 27)
        oled.show()
        j = 0
        raise TerpinalError("System Exit with 0 code")
    elif com == 'help':
        oled.fill(0)
        oled.show()
        i = 0
        coms = ['help: B', 'history: D', 'clear: A', 'exit: #', 'music 1-3: C']
        for rt in coms:
            oled.text(rt, 0, i)
            oled.show()
            i += 10
        j = 0
    elif com.find('music') != -1:
        num = int(com.replace('music', '')) - 1
        if num < len(melody):
            playsong(melody[num])
        i += 10
        j = 0
    elif com == 'history':
        oled.fill(0)
        oled.show()
        i = 0
        for ryw in history:
            oled.text(ryw, 0, i)
            oled.show()
            i += 10
        j = 0
    history.append(com)

oled.text("help - B,", 0, 0)
oled.text("enter - *", 0, 10)
oled.show()
i += 20

prog = ''
while True:
    key = keypadRead()
    if key == 'enter':
        code = prog
        prog = ''
        run(code)
    elif key != -1:
        prog += str(key)
        oled.text(key, j, i)
        oled.show()
        j += len(str(key)) * 10

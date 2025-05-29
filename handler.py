'''
Это основной файл для обработки команд терпинала.
Версия: 1.0
Команды: clear, help, music цифра, history, exit
'''
history = []
i = 0
j = 0

class TerpinalError(Exception):
    '''
    Ошибка терпинала.
    Нужна для выхода из системы.
    '''

def run(oled, melody, ps_fun, com):
    '''
    Запустить команду.
    Параметры:
    oled (SSD_1306_I2C): дисплей
    melody (list): список мелодий
    ps_fun (функция): функция, которая включает песню
    com (str): команда
    Возращает... Нечего
    '''
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
        if num < len(melody) or num > 0 or num == 0:
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

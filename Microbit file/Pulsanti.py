from microbit import *
import music
set_volume(0)

cont = 0
def mostra():
    global cont
    mat = Image('00000:'
                '00000:'
                '00000:'
                '00000:'
                '00000')
    if cont == 0:
        mat = Image('00900:'
                    '00900:'
                    '00000:'
                    '00900:'
                    '00900')
    elif cont == 1:
        mat = Image('00900:'
                    '00000:'
                    '00900:'
                    '00900:'
                    '00900')
    elif cont == 2:
        mat = Image('00900:'
                    '00900:'
                    '00000:'
                    '00900:'
                    '00900')
    elif cont == 3:
        mat = Image('00900:'
                    '00900:'
                    '00900:'
                    '00000:'
                    '00900')
        
    cont += 1
    if cont >= 4:
        cont = 0
    return mat
    
while True:
    if button_a.is_pressed() or button_b.is_pressed():
        vals = bool(button_a.is_pressed()),bool(button_b.is_pressed())
        print(vals)
        if button_a.is_pressed() and button_b.is_pressed():
            display.show(Image('80008:'
                               '08080:'
                               '00800:'
                               '08080:'
                               '80008'))
        else:
            display.show(mostra())
        music.set_tempo(bpm=500)
        music.play('a')
        

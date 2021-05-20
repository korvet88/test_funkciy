

def main():
    inputs()
    print(oper)



def inputs():
    counter = 0
    global oper
    while True:
        print("Введите операцию: s - для шифрования, d - для дешифрования")
        oper = input()
        if oper == "s" or oper == "d":
            counter = 0
            break
        else:
            counter += 1
        if counter == 5:
            print("Иди остынь и вводи верно!")
            return 0
    global languadge
    while True:
        print("Введите язык шифрования: rus - для русского языка, en - для английского языка")
        languadge = input()
        if languadge == "rus" or languadge == "en":
            counter = 0
            break
        else:
            counter += 1
        if counter == 5:
            print("Иди остынь и вводи верно!")
            return 0
    global step
    while True:
        print("Введите сдвиг: left - сдвиг влево, rigth - сдвиг вправо")
        step = input()
        if step == "left" or step == "rigth":
            counter = 0
            break
        else:
            counter += 1
        if counter == 5:
            print("Иди остынь и вводи верно!")
            return 0
    print("Вввод даннызх завершен")

def text():
    global eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    global eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    global rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    global rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

def programm(oper, languadge, step):

"""info aby"""
"""555 55 55 New if"""



main()
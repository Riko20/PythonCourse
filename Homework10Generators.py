# Задача-1
# У вас есть файл из нескольких строк. Нужно создать генератор который будет построчно выводить строки из вашего файла.
# При вызове итерировании по генератору необходимо проверять строки на уникальность.
# Если строка уникальна, тогда ее выводим на экран, если нет - скипаем

import time

file = "C:/Users/Dragonagek/Desktop/PythonCourse/text1.txt"
with open(file, 'r') as f:
    readlines = f.readlines()


def showstring():
    for readline in readlines:
        new = readline.replace('\n', '')
        yield new

def sort_string():
    listez = []
    gen = showstring()
    for i in gen:
        if i not in listez:
            listez.append(i)
            print(i)

sort_string()

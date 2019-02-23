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

# Задача-2 (оригинальный вариант и его делать не обязательно):
# представим есть файл с логами, его нужно бессконечно контролировать
# на предмет возникнования заданных сигнатур.
#
# Необходимо реализовать пайплайн из корутин, который подключается к существующему файлу
# по принципу команды tail, переключается в самый конец файла и с этого момента начинает следить
# за его наполнением, и в случае возникнования запиcей, сигнатуры которых мы отслеживаем -
# печатать результат
#
# Архитектура пайплайна

#                    --------
#                   /- grep -\
# dispenser(file) <- - grep - -> pprint
#                   \- grep -/
#                    --------

# Структура пайплайна:
# ```
import os
import io

def corout(func):
    def wrapper(*args, **kwargs):
        c = func(*args, **kwargs)
        c.send(None)
        return c
    return wrapper


@corout
def grep(sign, func):
    while True:
        x = yield
        if sign in x:
            print(type(func))
            func.send(sign)



@corout
def printer():
    while True:
        mess = yield
        print(mess)


@corout
def dispenser(greppe):
    while True:
        x = yield
        for grepp in greppe:
            grepp.send(x)



f_open = open('C:/Users/Dragonagek/Desktop/PythonCourse/text1.txt')

argum = [grep('Dave', printer()), grep('Martin', printer()), grep('Aloxa', printer())]
disp = dispenser(argum)


def follow(f_open, disp):
    while True:
        rl = f_open.readline()
        if not rl:
            break
        disp.send(rl)

follow(f_open, disp)

#Realization N2

def dis(f_op, sings):
    while True:
        rdl = f_op.readline()
        if not rdl:
            break
        yield from gr(rdl, sings)



def gr(rl, sings):
    for sing in sings:
        if sing in rl:
            yield from ppr(sing)
        else:
            pass

def ppr(s):
    while True:
        yield s
        break





def fol():
    ar = ['Aloxa', 'Dave', 'Martin']
    yield from dis(f_open, ar)



f = fol()
while True:
    print(next(f))

#Задача-3 (упрощенный вариант делаете его если задача 2 показалась сложной)
# Вам нужно создать pipeline (конвеер, подобие pipeline в unix https://en.wikipedia.org/wiki/Pipeline_(Unix)).
#
# Схема пайплайна :
# source ---send()--->coroutine1------send()---->coroutine2----send()------>sink
#
# Все что вам нужно сделать это выводить сообщение о том что было получено на каждом шаге и обработку ошибки GeneratorExit.
#
def source(where):
    a = 0
    while a < 10:
        try:
            a += 1
            where.send(a)
        except StopIteration:
            print("Corut1 is closed")
            break


@corout
def coroutine1(corut2):
    while True:
        val = yield
        try:
            print("Corut1, received: ", val)
            corut2.send(val)

        except (GeneratorExit, StopIteration):
            print("Corut2 is closed")
            break

@corout
def coroutine2():
    while True:
        val = yield
        print("Corut2, receeived: ", val)




cor2 = coroutine2()
cor1 = coroutine1(cor2)

source(cor1)
cor2.close()
source(cor1)
from string import punctuation
import string, re
import functools

#Задача-1
# Из текстового файла удалить все слова, содержащие от трех до пяти символов,
# но при этом из каждой строки должно быть удалено только четное количество таких слов.
def words_deleting(folder, finaltext):
    f = open(folder, "r")
    fintext = open(finaltext, "w")
    new = []               # list со словами, которые будем удалять, проверяем его на чет
    newlist = []           # список окончательно измененных предложений.
    mainlist = []          # список в котором содержатся предложения с файла

    appending_mainlist(f, mainlist)
    copy_for_deleting(mainlist, new, newlist)

    for elem in newlist:
        fintext.write("%s\n" % ' '.join(elem))


    f.close()
    fintext.close()




def appending_mainlist(f, mainlist):
    for line in f:
        regex = re.compile('[%s]' % re.escape(string.punctuation))                       #удаление пунктуации и добавление предложений в лист
        b = regex.sub('', line)
        mainlist.append(b)


def copy_for_deleting(mainlist, new, newlist):
    for lines in mainlist:
        index = 0
        l = lines.split()
        copylist = l.copy()                              # этот список является копией слов с предложений, с которого будут удаляться ненужные слова. Был создан для сохранения итерации
        for word in l:
            if len(word)>=3 and len(word) <= 5:
                index += 1
                copylist.remove(word)
                new.append(word)


        if len(new) % 2 == 0:
            new.clear()

        else:
            wordik = new.pop(index-1)
            copylist.insert(index-1, wordik)
            new.clear()

    newlist.append(copylist)




folder = "C:/Users/Dragonagek/PycharmProjects/Homework1/text1.txt"
finaltext = "C:/Users/Dragonagek/PycharmProjects/Homework1/finishedtext.txt"
words_deleting(folder, finaltext)

# Задача-2
# Текстовый файл содержит записи о телефонах и их владельцах.
# Переписать в другой файл телефоны тех владельцев, фамилии которых начинаются с букв К и С.

def contacter(f):

    file = open(f, "r")
    opened = file.readlines()
    file.close()
    return opened


def numbers_operations(opened):
    contlist = []
    surnames = []
    numbers = []

    for line in opened:
        contlist.append(line.split(", "))

    for list in contlist:
        surnames.append(list[1])
        numbers.append(list[0])

    return surnames, numbers

def resulting_func(surnames, numbers, writter):
    file_writer = open(writter, "w")
    index = 0
    for el in surnames:
        index += 1
        if el[0] == "К":
            a = "Номер {0}, Surname: {1}".format(numbers[index-1], el)
            file_writer.write(a)

    file_writer.close()


file = "C:/Users/Dragonagek/PycharmProjects/Homework1/contacts.txt"
writter = "C:/Users/Dragonagek/PycharmProjects/Homework1/contactstrue.txt"

cont = contacter(file)
surs, nums = numbers_operations(cont)
resulting_func(surs, nums, writter)


# Задача-3 - не обязательна к выполнению
# Написать декоратор который будет подавлять ошибки возникающие в теле вашей функции.
# Например ваша функция может иметь вид
def my_dec(func):
    def wrapper():
        try:
            a = func()
            print(a)
        except ValueError:
            print("ValueError dismissed")

    return wrapper

@my_dec
def my_func():
    raise ValueError("some text error")

my_func()

# Задача-4 - не обязательна к выполнению
# Написать декоратор c аргументом который будет подавлять определенные ошибки возникающие в теле вашей функции.
# Ошибки которые должен будет подавить ваш декоратор вы должны передать ему в качестве аргумента
def main_decor(error):
    def ins_decor(func):
        @functools.wraps(func)
        def wrapper():
            try:
                cache = func()
            except error:
                print(error, " interrupted")

        return wrapper
    return ins_decor

@main_decor(IndexError)
def function():
    cache = []
    a = cache.pop()
    return a

function()


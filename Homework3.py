# Задача-1
#
# Дан произвольный текст. Соберите все заглавные буквы в одно слово в том порядке как они встречаются в тексте.
# Например: текст = "How are you? Eh, ok. Low or Lower? Ohhh.", если мы соберем все заглавные буквы, то получим сообщение "HELLO".
def string_up(text):
    uplet = []
    for word in text:
        for letter in word:
            if letter.isupper():
                uplet.append(letter)
    str = ''.join(uplet[:])
    print(str)

string_up("How are you? Eh, ok. Low or Lower? Ohhh.")


# Задача-2
# Дан массив целых чисел. Нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд),
# затем перемножить эту сумму и последний элемент исходного массива.
# Не забудьте, что первый элемент массива имеет индекс 0.
nums = [1,2,3,4,5,6,67,8,9,20,32,35,24]

def find_zel(list):
    sum =0
    indexes = []
    for ind in range(len(list)):
        if ind%2 == 0:
            indexes.append(ind)
    for index in indexes:
        sum += list[index]

    last_elem = list[-1]
    fin = sum * last_elem
    print(fin)

find_zel(nums)


# Задача-3
# Дана строка и нужно найти ее первое слово.
# При решении задачи обратите внимание на следующие моменты:
#   1)В строке могут встречатся точки и запятые
#   2)Строка может начинаться с буквы или, к примеру, с пробела или точки
#   3)В слове может быть апостроф и он является частью слова
#   4)Весь текст может быть представлен только одним словом и все
stringa = ",.k al`oo"
def first_word(stringa):
    prescr = [',', '.', '?', '/']
    newl = []

    s = stringa.split()
    for one in s:
        for let in one:
            if let in prescr:
                break
            else:
                newl.append(one)

    return newl[0]


print(first_word(stringa))
# Задача-4
# Изменить исходную строку на новую строку в которой первый и последний символы строки поменяны местами.

old_string = 'It is the great day'
def change_string(old_string):
    newlist = []
    for words in old_string:
        for let in words:
            newlist.append(let)

    newlist[0], newlist[-1] = newlist[-1], newlist[0]
    newstring = ''.join(newlist)

    return newstring

print(change_string(old_string))


# Задача-5
# Дан тапл(tuple), необходимо его конвертнуть в стринг.
# Например:
# ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's') == 'exercises

tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')

def convert(tup):
    string = ''.join(tup)
    return string

print(convert(tup))


# **Задача-6 (Не обязательно, для тех кто скучает)
# You would like to set a password for a bank account. However, there are three restrictions on the format of the password:
#  1) it has to contain only alphanumerical characters (a−z, A−Z, 0−9);
#  2) there should be an even number of letters;
#  3) there should be an odd number of digits.

def set_pas(inp):
    digits = []
    lets = []
    prescr = [',', '.', '?', '/']

    for elem in inp:
        if elem in prescr:
            break
        else:
            if elem.isdigit():
                digits.append(elem)
            if elem.isalpha():
                lets.append(elem)

    if len(digits) % 2 == 0 :
        print("There should be odd number of digits. Please change password")
        return '0'
    if len(lets) % 2 != 0:
        print("there should be even number of letters. Please change password")
        return '0'
    else:
        print("Password correct")
        return inp



# You are given a string S consisting of N characters. String S can be divided into words by splitting it at, and removing, the spaces.
# The goal is to choose the longest word that is a valid password.
# You can assume that if there are K spaces in string S then there are exactly K + 1 words.
example_string = "test 5 a0A pass007 ?xy1"

def fing_the_longest(string):
    b = []
    a = string.split()
    for words in a:
        b.append(set_pas(words))

    print("The longest one: ", max(b, key = len))


fing_the_longest(example_string)




# For example, given "test 5 a0A pass007 ?xy1", there are five words and three of them are valid passwords: "5", "a0A" and "pass007".
# Thus the longest password is "pass007" and its length is 7.
# Note that neither "test" nor "?xy1" is a valid password, because "?" is not an alphanumerical character and "test" contains an even number of digits (zero).


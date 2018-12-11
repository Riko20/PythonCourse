import pprint
from itertools import groupby
from operator import itemgetter

#1)Дан массив из словарей 


data = [
    {'name': 'Viktor', 'city': 'Kiev', 'age': 30 },
    {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
    {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
    {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
    {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
    {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]

#1.1) отсортировать массив из словарей по значению ключа ‘age' 
def sort_dict(data):
    newlist = sorted(data, key=lambda k: k['age'])
    print ("1.1:  ",newlist)

sort_dict(data)


#1.2) сгруппировать данные по значению ключа 'city' 
# вывод должен быть такого вида :

def groupcity(data):
    if "__main__" == __name__:
        resulti = []
        for key, group in groupby(sorted(data, key=itemgetter('city')),
            key=itemgetter('city')):
            resulti.append({'city':key, "dat": [{k: v for k, v in dictionary.items() if k != "city"} \
                                                for dictionary in group]})
        pprint.pprint(resulti)

groupcity(data)

# 2) У вас есть последовательность строк. Необходимо определить наиболее часто встречающуюся строку в последовательности.
# Например:



def most_frequent(list_var):
    numlist = []
    for elem in list_var:
        numlist.append(list_var.count(elem))
    ind = numlist.index(max(numlist))
    ourstr = list_var[ind]
    return ourstr

print ("2:  ", most_frequent(['a', 'a', 'bi', 'bi', 'bi','d','d','d','d','d','d','d']))

# 3) Дано целое число. Необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.

a = 123405
multipl = 1
while a>0:
    if a%10 != 0:
        multipl *= a%10
    a = a // 10
print("3:  ", multipl)

# 4) Есть массив с положительными числами и число n (def some_function(array, n)).
# Необходимо найти n-ую степень элемента в массиве с индексом n. Если n за границами массива, тогда вернуть -1.
array = [1,2,3,4,5,6,7,8,9]


def arrayret(array, n):
    if n not in array:
        return -1
    res = array[n] ** n
    print(res)


arrayret(array, 6)
# =======================================================
# 5) Есть строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).

def stringint(stringa):
    counter = 0
    a = stringa.split()
    for elem in a:
        if elem.isalpha():
            counter += 1
        if elem.isdecimal():
            counter =0
        if counter == 3:
            print('It`s true')


stringint('hello 1 one two three 15 world')
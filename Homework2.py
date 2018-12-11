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


# Задача-1
# У вас есть список(list) IP адрессов. Вам необходимо создать
# класс который будет иметь методы:
# 1) Получить список IP адресов
# 2) Получить список IP адресов в развернутом виде
# (10.11.12.13 -> 13.12.11.10)
# 3) Получить список IP адресов без первых октетов
# (10.11.12.13 -> 11.12.13)
# 4) Получить список последних октетов IP адресов
# (10.11.12.13 -> 13)
#

import json


class WorkIp(object):
    listwithoutfirst = []  # list without first octets
    list_last = []
    newdict = []
    alwaysdict = []

    def __init__(self, list):
        self.list = list

    def get_iplist(self):
        return self.list

    def getip_without_first(self):
        for ip in self.list:
            ipnew = ip[3:]
            self.listwithoutfirst.append(ipnew)

        return self.listwithoutfirst

    def getreverseip(self):

        for el in self.list:
            element = el.split('.')
            for every in element:
                self.newdict.append(every)
            for n in range(len(self.newdict)):
                c = self.newdict.pop()
                self.newdict.insert(n, c)
            string_of_dig = '{0}'.format('.'.join(self.newdict[0:4]))  # строки с правильной последовательностью цифр из айпи

            self.alwaysdict.append(string_of_dig)
            self.newdict.clear()

        return self.alwaysdict

    def get_last(self):
        for ip in self.list:
            ipnew = ip[(len(ip) - 2):]
            self.list_last.append(ipnew)
        return self.list_last


list = ['10.11.12.13', '11.12.13.14', '15.16.17.18']

ipwnik = WorkIp(list)

print(ipwnik.get_last())
print(ipwnik.getip_without_first())

print(ipwnik.getreverseip())

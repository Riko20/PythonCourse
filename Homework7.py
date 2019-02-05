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


# Задача-2
# У вас несколько JSON файлов. В каждом из этих файлов есть
# произвольная структура данных. Вам необходимо написать
# класс который будет описывать работу с этими файлами, а
# именно:
# 1) Запись в файл
# 2) Чтение из файла
# 3) Объединение данных из файлов в новый файл
# 4) Получить путь относительный путь к файлу
# 5) Получить абсолютный путь к файлу
import os, json

class WorkingJson:

    def __init__(self, file):
        self._file = file

    def filling_file(self, newfile, newinf):
        self._newfile = newfile
        self._newinf = newinf
        with open(self._newfile, 'w') as f:
            json.dump(self._newinf, f)

    def reading(self):
        with open(self._file) as f:
            data = json.load(f)
            return data

    def compicating(self, anfile, olddata, newdata):
        self._anfile = anfile
        olddata.update(newdata)
        with open(self._anfile, 'w') as f:
            json.dump(olddata, f, indent=2)

    def getting_relpath(self):
        return (os.path.relpath(self._file))

    def getting_absolpass(self):
        return (os.path.abspath(self._file))


file = 'C:/Users/Dragonagek/Downloads/data.json'
file2 = 'C:/Users/Dragonagek/Desktop/PythonCourse/states_titlecase.json'
file_for_filling = 'C:/Users/Dragonagek/Desktop/PythonCourse/newjson1.json'
file_for_compl = 'C:/Users/Dragonagek/Desktop/PythonCourse/together.json'

work_json = WorkingJson(file2)
first_readed = work_json.reading()
print('First readed file: {}'.format(first_readed))

work_json1 = WorkingJson(file)
second_readed = work_json1.reading()
print('Second readed file: {}'.format(second_readed))

newinfo = {"krai":[{'name': 'Ukraine', 'abbreviation': 'UA'}]}
work_json1.filling_file(file_for_filling, newinfo )


work_json.compicating(file_for_compl, first_readed, second_readed)
print("File that was complicated: {}".format(WorkingJson(file_for_compl).reading()))

relpath = work_json.getting_relpath()
print("Realpath: {}".format(relpath))


abspath = work_json.getting_absolpass()
print("Absolute pass: {}".format(abspath))


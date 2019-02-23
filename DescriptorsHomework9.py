from weakref import WeakKeyDictionary
import re


class EmailDescriptor:
    def __init__(self):
        self.data = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.data[instance]

    def __set__(self, instance, value):
        self.data[instance] = value
        if len(self.data[instance]) > 7:
            if re.match("^.+@([?)[a-zA-Z0-9-.]+.(\w)$)", self.data[instance]) is not None:
                return self.data[instance]
            else:
                raise NameError('{} is not correct'.format(self.data[instance]))


class MyClass:
    email = EmailDescriptor()


my_class = MyClass()
my_class.email = "validemail@gmail.com"
print(my_class.email)

my_class.email = "novalidemail"
print(my_class.email)

# Задача-2
# Реализовать синглтон метакласс(класс для создания классов синглтонов).

class Singleton(type):
    _singleton = None

    def __call__(self, *args, **kwargs):
        if not self._singleton:
            self._singleton = super(MyClass,self).__new__(self)
        return self._singleton



class MyClass(metaclass=Singleton):
    print("what is there")


myclass = MyClass()
wooo = MyClass()


assert id(myclass) == id(wooo)

# Задача-3
# реализовать дескриптор IngegerField(), который будет хранить уникальные
# состояния для каждого класса где он объявлен

class IngegerField(object):

    def __init__(self):
        self.conditions = WeakKeyDictionary

    def __get__(self, instance, owner):
        if instance is None:
            return self

        return self.conditions[instance]

    def __set__(self, instance, value):
        self.conditions[instance] = value


class Data:
    desc = IngegerField()


data_raw = Data()
new_data_raw = Data()

data_raw.number = 10

new_data_raw.number = 20

assert data_raw.number != new_data_raw.number
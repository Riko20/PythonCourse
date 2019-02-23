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
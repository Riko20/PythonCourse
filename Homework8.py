# Задача-1
# Доделать задачу 2 которую вы получили на практике

import os
from contextlib import contextmanager


class Manager(object):
     def __init__(self, path, exception):
         self.exception = exception
         self.path = path
         self.saved_cwd = None

     def __enter__(self):
         self.saved_cwd = os.getcwd()
         os.chdir(self.path)

     def __exit__(self, exc_type, exc_val, exc_tb):
         os.chdir(self.saved_cwd)
         a = exc_type is not None and issubclass(exc_type, self.exception)
         return a


path = 'C:/Users/Dragonagek/Downloads'
path2 = 'C:/Users/Dragonagek/Desktop/PythonCourse'
manager = Manager(path2, Exception)

with manager as f:
    print('okay')
    raise ValueError("Some value error")

#Задача -2
# Описать задачу выше но уже с использованием @contexmanager

@contextmanager
def change_except(path, exc):
    try:
        cwd = os.getcwd()
        os.chdir(path)
        yield
    except exc:
        print("Some exception {}".format(exc))
    finally:
        os.chdir(cwd)

with change_except(path2, Exception):
    raise KeyError("tak to")



# Задача -3
# Создать менеджер контекста который будет подсчитывать время выполняния блока инсрукций

import time


class Open_File(object):
    time1 = time.time()

    def __init__(self, path):
        self.path = path
        self.cwd = os.getcwd()

    def __enter__(self):
        os.chdir(self.path)
        first_path = os.listdir()
        for i in first_path:
            print(i)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.cwd)
        a = os.listdir()
        for i in a:
            print(i)
        time2 = time.time()
        print('spent time for operation: {} '.format(time2 - self.time1))


open_this = Open_File(path)

with open_this:
    print("What is in file?")
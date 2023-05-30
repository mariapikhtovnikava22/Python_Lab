# from PikhtovSerLib.json_serealazer import JsonSerelizator
# # import constants
# # import math
# # from inspect import getmembers
# # import regex
# # from constants import *
# # import json
# # from my_serelizator import Serelizator

import PikhtovSerLib
class MyClass:
    def __init__(self):
        self.numbers = [1, 2, 3, 4, 5]

    def square_numbers(self):
        squared = list(map(lambda x: x ** 2, self.numbers))
        return squared


my_obj = MyClass()

j = PikhtovSerLib.JsonSerelizator()
d_s = j.dump(my_obj, "test.json")
ds_d = j.load("test.json")

js = PikhtovSerLib.XMLSerelizator()
x = js.dump(my_obj, 'test_xml.xml')
x_ds = js.load('test_xml.xml')

print(ds_d.square_numbers())

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value


class MyClass:
    def __init__(self, data):
        self.data = data

    def iterate_with_iterator(self):
        iterator = MyIterator(self.data)
        for item in iterator:
            print(item)

    def iterate_with_generator(self):
        for item in self.data_generator():
            print(item)

    def data_generator(self):
        for item in self.data:
            yield item


ser2 = MyClass([1, 2, 3])

j2 = PikhtovSerLib.JsonSerelizator()

ser2_s = j2.dumps(ser2)
sser = j2.loads(ser2_s)

print(sser.iterate_with_generator())

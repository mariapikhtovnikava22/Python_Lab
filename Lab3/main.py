from json_serealazer import JsonSerelizator
import math
from inspect import getmembers

from constants import *
import json


# k = 5
# dictor = {'do': 1, 'cos': 3}
def my_function():
    def go():
        x = 10
        y = (20)
        return x + y

    return go()


l = lambda n: n + 25


m = 5
n = 3
def sums():
    return m + n


class A:
    a = 5
    b = 6
    def sum(self):
        return self.a + self.b


a = JsonSerelizator()
# print(a.dumps(dictor))
# print(a.loads(a.dumps(dictor)))
# print(my_function())
b = a.dumps(A)
print(b)
# f = a.loads(b)
# d = f()

g = A()

print(g.sum())


print(sums())


from json_serelalizator import JsonSerelizator
import math
from inspect import getmembers

from constants import *


# k = 5
# dictor = {'do': 1, 'cos': 3}
def my_function():
    def go():
        x = 10
        y = (20)
        return x + y

    return go()


l = lambda n: n + 25

a = JsonSerelizator()
# print(a.dumps(dictor))
# print(a.loads(a.dumps(dictor)))
# print(my_function())
b = a.dumps(my_function)
print(b)
f = a.loads(b)
print(f())

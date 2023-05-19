from json_serelalizator import JsonSerelizator
from math import sqrt

from constants import*
k = 5
def my_function():
    x = 10
    y = 20
    return x + y - k


a = JsonSerelizator()

b = a.dumps(my_function)
v = a.loads(b)


print(v())
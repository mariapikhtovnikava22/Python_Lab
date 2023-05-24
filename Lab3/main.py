from json_serealazer import JsonSerelizator
import math
from inspect import getmembers

from constants import *
import json

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("func start")
        res = func(*args, **kwargs)
        print("Func end")
        return res
    return wrapper

X = 12
class A:
    bob = "sinii"

    @staticmethod
    def ret_bob():
        return A.bob

    def my_method(self, x):
        return x + 5

class B:
    @staticmethod
    @my_decorator
    def another_method(k):
        print("Hi:)")
        return math.sin(k * X)

class C(A, B):
    def __init__(self):
        self.coca = "Cola"


a = JsonSerelizator()

f = C()

f_ser = a.dumps(f)
print(f_ser)
f_deser = a.loads(f_ser)
print(f_deser.my_method(5))




from json_serelalizator import JsonSerelizator
import json

s = 5


def my_function():
    x = 10
    y = 20
    return x + y


a = JsonSerelizator()
print(a.dumps(my_function))

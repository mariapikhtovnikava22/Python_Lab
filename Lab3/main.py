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


file_from = "test.json"
file_to = "test_xml.xml"
format_from = "json"
format_to = "xml"

from_serializer = PikhtovSerLib.Choice.create_serializer(format_from)
to_serializer = PikhtovSerLib.Choice.create_serializer(format_to)


obj = from_serializer.load(file_from)
to_serializer.dump(obj, file_to)


# def my_dec(count):
#     def my_decor(func):
#         def check(*args, **kwargs):
#             if len(args) + len(kwargs) > count:
#                 print("fo")
#             return func(*args, **kwargs)
#         return check
#     return my_decor
#
# @my_dec(2)
# def funct(*args):
#
#    print("d")
#
#
# d = funct(1, 2, 3)
#
#
class MyContextManager:
    def __enter__(self):
        print("Entering the context")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            return True
        else:
            print("By")


with MyContextManager() as cm:
    print(1/0)
    print("Inside the context")


# class MyException(Exception):
#     def __init__(self, message):
#         self.message = message
#
#     def __str__(self):
#         return self.message

# try:
#     raise MyException("Это мое исключение")
# except MyException as e:
#     print(e)

# class My_Itearor:
#     def __init__(self, colection):
#         self.colection = colection
#         self.cuurent = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.cuurent < len(self.colection):
#             val = self.colection[self.cuurent]
#             self.cuurent = self.cuurent + 1
#             return val
#         else:
#             raise StopIteration
#
#
# a = [1, 2, 3, 3]
# it = My_Itearor(a)
# print(it.__iter__())
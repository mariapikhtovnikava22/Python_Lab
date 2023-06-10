# class A(type):
#
#
#     def __new__(cls, *args, **kwargs):
#         super.__new__(cls)
#         return cls
#
#
#     def __call__(self, *args, **kwargs):


# def check(*args):
#     d = tuple()
#     if isinstance(args, int):
#         d = args
#         type('A', (), {*args})


def decor(func):
    dic = {}

    def wrapper(num):
        res = func(num)
        if num in dic.keys():
            print("Hi")
            return func(num)
        else:
            dic[num] = res
            return func(num)

    return wrapper


@decor
def ru(a):
    return a + 4


print(ru(4))
print(ru(4))

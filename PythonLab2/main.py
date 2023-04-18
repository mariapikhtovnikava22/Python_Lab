from parse import parser, clear_many_signs
from re import findall
from container import Container

# parser()

# s = "Cool! Do this . . . Clear!!!"
#
# print(s)
#
# s = clear_many_signs(s)
#
# print(s)

h1 = Container(2, 3, 4, 5)
h2 = Container(3, 5, 6, 7)

print(h1.__iadd__(h2))

# print(h1.get_List_elements())


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
h1.add("Sol", 4, 7)
res = h1.grep(r"4")
print(res)

print(h1.get_List_elements())



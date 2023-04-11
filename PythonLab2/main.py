from parse import clear_abbrev, NonDeclarativeSentences, DeclarativeSentences, clear_other, clear_points, clear_num

s = ""
print("Please enter a text(finish typing by pressing Enter after Ctrl+D): ")

try:
    while True:
        line = input()
        s += line + "\n"
except EOFError:
    pass


result = clear_abbrev(s)

print(result)


if len(result) == 0:
    NonDeclarativeSentences(s)
    DeclarativeSentences(s)
else:
    NonDeclarativeSentences(result)
    DeclarativeSentences(result)





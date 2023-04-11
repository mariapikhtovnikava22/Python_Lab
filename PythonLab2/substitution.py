from re import sub
def change_list(iterate_str, what_find, rep):

    resul = []
    for r in iterate_str:
        resul.append(sub(what_find, rep, r))
    return resul
def change_str(iterate_str, where, what_find):
    print(what_find)
    for i, r in enumerate(what_find):
        print(r, i, what_find, iterate_str[i])
        where = where.replace(r, iterate_str[i])

    return where


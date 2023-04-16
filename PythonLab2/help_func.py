from re import sub, findall
from constants import word_pattern


def change_list(iterate_str, what_find, rep):
    resul = []
    for r in iterate_str:
        resul.append(sub(what_find, rep, r))
    return resul


def change_str(iterate_str, where, what_find):
    for i, r in enumerate(what_find):
        where = where.replace(r, iterate_str[i])
    return where


def Col_of_word(sentence):
    col_word = 0
    for r in sentence:
        col_word += len(find_word(r))  # список слов в 1-м предложении
    return col_word


def len_symb(sentence):
    len_symbols = sum(len(w) for r in sentence for w in find_word(r))
    return len_symbols


def find_word(test_str):
    res = findall(word_pattern, test_str)
    return res

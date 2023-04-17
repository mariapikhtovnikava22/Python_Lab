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
        # print(find_word(r))
    return col_word


def len_symb(sentence):
    len_symbols = sum(len(w) for r in sentence for w in find_word(r))
    return len_symbols

def find_word(test_str):
    res = findall(word_pattern, test_str)
    return res

def make_list_of_ngrams(test_str, n):
    list_of_ngram = []
    if not n:
        list_of_ngram.append(test_str)

    else:
        lst_word = [x.lower() for x in find_word(test_str)]
        # print(lst_word)
        for i, r in enumerate(lst_word):

            if i + n <= len(lst_word):
                list_of_ngram.append(lst_word[i:n + i])
            else:
                break

    return list_of_ngram


def make_dict_ofNgram(test_str, n):
    list_of_ngram = make_list_of_ngrams(test_str, n)
    dict_of_ngram = {}
    num_of_repetit = 0

    for i in range(len(list_of_ngram)):
        for j in range(len(list_of_ngram)):
            if str(list_of_ngram[i]).lower() == str(list_of_ngram[j]).lower():
                num_of_repetit += 1
                dict_of_ngram.update({str(list_of_ngram[i]): num_of_repetit})
        num_of_repetit = 0

    print(f"List of ngrams and how many times this ngrams occur\n {dict_of_ngram}")
    return dict_of_ngram


def Top_Ngram(test_str, n, k):
    if not k:
        dict_of_ngram = make_dict_ofNgram(test_str, n)
        print("Oops. You entered the size of the top equal to 0. Therefore, it will not be displayed")
        return

    dict_of_ngram = make_dict_ofNgram(test_str, n)
    res_dict = {}

    maximum = 0
    key_help = ""

    while k:
        if len(dict_of_ngram) == 0:
            break
        for key, value in dict_of_ngram.items():
            if maximum < value:
                maximum = value
                key_help = key

        res_dict.update({key_help: maximum})
        dict_of_ngram.pop(key_help, maximum)
        maximum = 0
        k -= 1

    return res_dict

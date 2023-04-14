from constants import*
from re import sub, findall, split
from help_func import*

from collections import OrderedDict
def clear_points(test_str):
    res = sub(ThreeSigns, lambda match: match.group(1)[0], test_str)
    return res

# Функция для замены точки на пробел
def replace_dot_with_space(match):
    return match.group(0).replace('.', ' ')
def clear_num(test_str):
    res = sub(numbers_pattern, replace_dot_with_space, test_str)
    return res
def clear_other(test_str):

    res = findall(other_abbreviate, test_str)
    if not res:
        return []
    return res
def clear_abbrev(test_str):

    result = clear_num(test_str)
    points = clear_points(result)
    res = findall(Abbreviate, points) + clear_other(points)
    resul = change_list(res, r"\.", ' ')
    result = change_str(resul, points, res)
    result = sub(r"\n", "", result)
    return result

def DeclarativeSentences(test_str):
    col = split(r"\.", test_str)
    return col

def NonDeclarativeSentences(test_str):
    col = split(r"\!|\?", test_str)
    return col

def find_word(test_str):
    res = findall(word_pattern, test_str)
    return res

def average_len(test_str):

    list_of_col = []
    col_of_word = 0
    len_symbols = 0

    sentence = split(r"\.|\!|\?", test_str)
    sentence = sentence[:-1] #срез

    for r in sentence:
        col_word = find_word(r) #список слов в 1-м предложении
        for w in col_word:
            len_symbols += len(w)
        #list_of_col.append(col_word)
        col_of_word += len(col_word)

    print(col_of_word)
    # print(list_of_col)
    print(len_symbols)
    print(len(sentence))
    aver_len_sentence = len_symbols/len(sentence)
    # print(list_of_col)

    aver_len_word = len_symbols/col_of_word
    return aver_len_sentence, aver_len_word

def clear_direct_speech(test_str):

    res = findall(direct_speech_pat, test_str)


def ngrams(test_str, n, k):

    list_of_ngram = []

    lst_word = [x.lower() for x in find_word(test_str)]
    print(lst_word)

    for i, r in enumerate(lst_word):

        if i+n <= len(lst_word):
            list_of_ngram.append(lst_word[i:n+i])
        else:
            break

    print(list_of_ngram)

    ''' 
    Создаем словарь, где ключ список n-грамм, значение кол-во ее вхождений в тексте
    потом сортируем его и выводим последовательность 
    
    
    '''

    dict_of_ngram = {}

    num_of_rep = 0

    for i in range(len(list_of_ngram)):
        for j in range(len(list_of_ngram)):
            if str(list_of_ngram[i]).lower() == str(list_of_ngram[j]).lower():
                num_of_rep += 1
                dict_of_ngram.update({str(list_of_ngram[i]): num_of_rep})
        num_of_rep = 0

    print(dict_of_ngram)

    res_dict = {}

    maximum = 0
    key_help = ""

    while k:
        for key, value in dict_of_ngram.items():
            if maximum < value:
                maximum = value
                key_help = key

        res_dict.update({key_help: maximum})
        dict_of_ngram.pop(key_help, maximum)
        maximum = 0
        k -= 1

    print(res_dict)

    


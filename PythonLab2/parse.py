from constants import*
from re import sub, findall, split
from help_func import*

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
    # res = findall(other_abbreviate, test_str)
    # print(res)
    res = sub(other_abbreviate, replace_dot_with_space, test_str)
    if not res:
        return []
    return res
def clear_abbrev(test_str):

    result = clear_num(test_str)
    points = clear_points(result)
    other = clear_other(points)
    res = findall(Abbreviate, other)
    resul = change_list(res, r"\.", ' ')
    result = change_str(resul, other, res)
    # print(result)
    result = sub(r"\n", "", result)
    return result
def get_user_inp():
    test_str = ''

    print("Please enter a text(enter 'стоп' to complete): ")

    while True:
        line = input()
        if not line:  # Проверяем, что строка пустая
            print("You have not entered the text please try again.")
            continue
        if line == "стоп":
            break
        test_str += line + "\n"

    return test_str
def parse():

    test_str = get_user_inp()

    if not len(test_str):
        print("You didn't enter anything :(")
        print(f"Col of declarative sentences: 0\n"
              f"Col of non-declarative sentences: 0")
        print(f"Average length of the sentence in characters(words count only): 0\n"
              f"Average length of the word in the text in characters: 0")
        return

    test_str = clear_abbrev(test_str)

    dcol = len(DeclarativeSentences(test_str)) - 1
    ncol = len(NonDeclarativeSentences(test_str)) - 1
    if dcol+ncol == 0:
        print("You have not entered a single sentence")
        return
    else:
        print(f"Col of declarative sentences: {dcol}\n"
              f"Col of non-declarative sentences: {ncol}")
        av_len_sent, aver_len_word = average_len(test_str)
        print(f"Average length of the sentence in characters(words count only): {av_len_sent}\n"
              f"Average length of the word in the text in characters: {aver_len_word}")
        k = input("Enter top size: ")
        n = input("Enter the number of top: ")
        ngrams(test_str, n, k)



def DeclarativeSentences(test_str):
    sentence = split(r"\.", test_str)
    print(sentence)
    return sentence
def NonDeclarativeSentences(test_str):
    sentence = split(r"\!|\?", test_str)
    print(sentence)
    return sentence
def average_len(test_str):

    sentence = split(r"\.|\!|\?", test_str)
    sentence = sentence[:-1]#срез

    col_of_word = Col_of_word(sentence)
    len_symbols = len_symb(sentence)
    print(f"Number of words in the text: {col_of_word}")

    print(f"Number of symbols in the text: {len_symbols}")

    aver_len_sentence = len_symbols / len(sentence)
    aver_len_word = len_symbols / col_of_word
    return aver_len_sentence, aver_len_word

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

    print(res_dict)


    


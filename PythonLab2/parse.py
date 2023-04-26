from constants import *
from re import sub, findall, split
from help_func import *
from for_input import input_, get_user_inp

def clear_many_signs(test_str):
    # print(findall(ThreeSigns, test_str))
    res = sub(ThreeSigns, lambda match: match.group(1)[0], test_str)
    return res


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
    points = clear_many_signs(result)
    other = clear_other(points)
    res = findall(Abbreviate, other)
    resul = change_list(res, r"\.", ' ')
    result = change_str(resul, other, res)
    # print(result)
    result = sub(r"\n", "", result)
    return result

def print_empty_parse():
    print(f"Col of declarative sentences: 0\n"
          f"Col of non-declarative sentences: 0")
    print(f"Average length of the sentence in characters(words count only): 0\n"
          f"Average length of the word in the text in characters: 0")


def parser():
    test_str = get_user_inp()

    if not len(test_str):
        print("You didn't enter anything :(")
        print_empty_parse()
        return

    test_str = clear_abbrev(test_str)

    dcol = len(DeclarativeSentences(test_str)) - 1
    ncol = len(NonDeclarativeSentences(test_str)) - 1

    if dcol + ncol == 0:
        print("You have not entered a single sentence")
        print_empty_parse()
        return

    else:
        if not find_word(test_str):
            print("Your text does not contain a single word!")
            print(f"Number of words in the text: 0")
            print(f"Number of symbols in the text: 0")
            print_empty_parse()
            return

        print(f"Col of declarative sentences: {dcol}\n"
              f"Col of non-declarative sentences: {ncol}")
        # print(test_str)
        av_len_sent, aver_len_word = average_len(test_str)
        print(f"Average length of the sentence in characters(words count only): {av_len_sent}\n"
              f"Average length of the word in the text in characters: {aver_len_word}")

        print("Enter top size: ")
        k = input_(int)
        print("Enter the number of top: ")
        n = input_(int)
        ngrams(test_str, n, k)
        return


def DeclarativeSentences(test_str):
    sentence = split(r"\.", test_str)
    return sentence


def NonDeclarativeSentences(test_str):
    sentence = split(r"\!|\?", test_str)
    return sentence


def average_len(test_str):
    sentence = split(r"\.|\!|\?", test_str)
    sentence = sentence[:-1]  # срез

    col_of_word = Col_of_word(sentence)
    len_symbols = len_symb(sentence)

    print(f"Number of words in the text: {col_of_word}")

    print(f"Number of symbols in the text: {len_symbols}")

    aver_len_sentence = len_symbols / len(sentence)
    aver_len_word = len_symbols / col_of_word
    return aver_len_sentence, aver_len_word


def ngrams(test_str, n, k):
    res_dict = Top_Ngram(test_str, n, k)
    print(res_dict)

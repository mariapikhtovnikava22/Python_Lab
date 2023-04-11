from constants import Abbreviate, ThreeSigns, other_abbreviate, numbers_pattern
from re import sub, findall, split
from substitution import change_str, change_list

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

    # if not res:
    #     return ""

    resul = change_list(res, r"\.", ' ')
    result = change_str(resul, points, res)
    return result

def DeclarativeSentences(test_str):
    col = findall(r"\.", test_str)
    print(len(col))

def NonDeclarativeSentences(test_str):
    col = findall(r"\!|\?", test_str)
    print(len(col))

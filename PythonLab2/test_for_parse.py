import unittest

from help_func import find_word
from parse import clear_abbrev, clear_num, clear_many_signs,\
    parser, DeclarativeSentences, NonDeclarativeSentences, average_len, ngrams, \
    make_dict_ofNgram, make_list_of_ngrams, Top_Ngram, find_word, Col_of_word, len_symb


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.THREE_SIGNS_TST = "So cool!!! How are u? ? ? I can help you... And I like it. . . It is sщ easy?! " \
                               "Home!!!!!!!!!!!! I know that is so fine? !"
        self.THREE_SIGNS_RES = "So cool!How are u?I can help you.And I like it.It is sщ easy?" \
                               "Home!I know that is so fine?"

        self.Abbrev_TST = "Mrs.Smit Ms.Smir. Mr.Dim, 23p.m.Doctor! kof@mail.ru "
        self.Abbrev_RES = "Mrs Smit Ms Smir.Mr Dim, 23p m.Doctor!kof@mail ru "

        self.NUM_TST = "Good day my dear! I hope you got an answer equal to 46.5675 in the last example"
        self.NUM_RES = "Good day my dear! I hope you got an answer equal to 46 5675 in the last example"

        self.WORD_LIST_TST = "Mrs.Smit Ms.Smir. Mr.Dim, 23p.m.Doctor! kof@mail.ru 76854 hj8kj"
        self.WORD_LIST_RES = ["Mrs", "Smit", "Ms", "Smir", "Mr", "Dim", "23p", "m", "Doctor",
                              "kof", "mail", "ru", "hj8kj"]

        self.COLW_LIST_TST = ["Mrs Smit Ms Smir", "Mr Dim, 23p m", "Doctor", "kof@mail ru 76854 hj8kj"]
        self.COLW_LIST_RES = 13



    def test_clear_many_signs(self):
        self.assertEqual(clear_many_signs(self.THREE_SIGNS_TST), self.THREE_SIGNS_RES)

    def test_clear_abbrev(self):
        self.assertEqual(clear_abbrev(self.Abbrev_TST), self.Abbrev_RES)

    def test_clear_num(self):
        self.assertEqual(clear_num(self.NUM_TST), self.NUM_RES)

    def test_find_word(self):
        self.assertEqual(find_word(self.WORD_LIST_TST), self.WORD_LIST_RES)

    def test_Col_word(self):
        self.assertEqual(Col_of_word(self.COLW_LIST_TST), self.COLW_LIST_RES)

if __name__ == '__main__':
    unittest.main()

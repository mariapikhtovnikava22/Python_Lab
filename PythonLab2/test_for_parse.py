import unittest
from parse import clear_abbrev, clear_num, clear_many_signs,\
    DeclarativeSentences, NonDeclarativeSentences, average_len, \
    make_list_of_ngrams, Top_Ngram, find_word, Col_of_word, len_symb


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

        self.COL_SYM_LIST_TST = ["Mrs Smit Ms Smir", "Mr Dim, 23p m", "Doctor", "kof@mail ru 76854 hj8kj"]
        self.COL_SYM_LIST_RES = 42

        self.AVER_LEN_TST = "Mrs Smit Ms Smir.Mr Dim, 23p m.Doctor!kof@mail ru. Super day?"
        self.AVER_LEN_RES = 45/5, 45/14


        self.DECLAR_SENTENCES_TST = "Mrs Smit Ms Smir.Mr Dim, 23p m.Doctor!kof@mail ru. Super day???"
        self.DECLAR_SENTENCES_RES = len(["Mrs Smit Ms Smir", "Mr Dim, 23p m", "Doctor!kof@mail ru", " Super day???"])

        self.NON_DEC_SENTENCES_TST = "Mrs Smit Ms Smir.Mr Dim, 23p m.Doctor!kof@mail ru. Super day?"
        self.NON_DEC_SENTENCES_RES = len(["Mrs Smit Ms Smir.Mr Dim, 23p m.Doctor", "kof@mail ru. Super day", ""])

        self.LIST_NGRAMS_TST = "Good day my dear! I hope you got an answer equal to 46.5675 in the last example"
        self.LIST_NGRAMS_RES = [["good", "day"], ["day", "my"], ["my", "dear"], ["dear", "i"], ["i", "hope"], ["hope", "you"],
                                ["you", "got"], ["got", "an"],
                                ["an", "answer"], ["answer", "equal"], ["equal", "to"], ["to", "in"], ["in", "the"],
                                ["the", "last"], ["last", "example"]]

        self.TOP_NGRAM_TST = "Good day my dear. Tomorrow also will be good day. also will cool hop, pold good day"
        self.TOP_NGRAM_RES = {"['good', 'day']": 3, "['also', 'will']": 2}

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

    def test_Len_Symb(self):
        self.assertEqual(len_symb(self.COL_SYM_LIST_TST), self.COL_SYM_LIST_RES)

    def test_declar_sentences(self):
        self.assertEqual(len(DeclarativeSentences(self.DECLAR_SENTENCES_TST)), self.DECLAR_SENTENCES_RES)

    def test_NONdecylar_sentences(self):
        self.assertEqual(len(NonDeclarativeSentences(self.NON_DEC_SENTENCES_TST)), self.NON_DEC_SENTENCES_RES)

    def test_make_list_of_ngrams(self):
        self.assertEqual(make_list_of_ngrams(self.LIST_NGRAMS_TST, 2), self.LIST_NGRAMS_RES)

    def test_top_ngram(self):
        self.assertEqual(Top_Ngram(self.TOP_NGRAM_TST, 2, 2), self.TOP_NGRAM_RES)

    def test_aver_len(self):
        self.assertEqual(average_len(self.AVER_LEN_TST),self.AVER_LEN_RES)


if __name__ == '__main__':
    unittest.main()

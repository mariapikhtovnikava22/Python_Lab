from parse import *

# s = ""
# print("Please enter a text(finish typing by pressing Enter after Ctrl+D): ")
#
# try:
#     while True:
#         line = input()
#         s += line + "\n"
# except EOFError:
#     pass

# s = ''' Dr. Livesey said, "The log cabin is not visible from the ship. They must be aiming at a flag. We must load a flag advance."
# The word "rum" and the word "death" mean the same thing to you.
# Where's the map, Billy?
# The devil is with them! It's been over hours! It's getting a little boring. . .
# Billy Bones, aka "Captain". The owner of the Treasure Island map, which started it all.
# He drinks a lot and always has a cold. Bad character. Not married.
# "The chest contains gold, diamonds, etc.," Billy said.
# Gold, diamonds, etc. not interested for me. We need a map!
# "Come to me at 7p.m.," he said to Jim. '''
#
# s2 = """The word "rum" and the word "death" mean the same thing to you."""
# sentences = nltk.sent_tokenize(s)
#
# # Подсчет количества предложений
# num_sentences = len(sentences)
#
# print("Количество предложений:", num_sentences)

# result = clear_abbrev(s)
#
# col = average_len(result)
#
# print(col)
#
# resul = ngrams(s, 2, 3)

parse()

# if not len(result):
#
#     NonDeclarativeSentences(s)
#     DeclarativeSentences(s)
#
# else:
#     col1 = NonDeclarativeSentences(result)
#
#     if col1[len(col1)-1] == '':
#         print(col1, '\n', len(col1)-1)
#     print(col1, '\n', len(col1) - 1)
#
#     col2 = DeclarativeSentences(result)
#
#     if col2[len(col2) - 1] == '':
#         print(col2, '\n', len(col2) - 1)
#     print(col2, '\n', len(col2) - 1)





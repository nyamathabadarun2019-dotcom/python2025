"""
Problem:
Count the frequency of each word in a sentence.

"""

sentence = "python is easy and python is powerful"

words = sentence.split()
word_frequency = dict(map(lambda w: (w, words.count(w)), set(words)))

print("Word Frequency:")
print(word_frequency)

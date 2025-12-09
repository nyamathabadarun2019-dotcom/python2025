# 1. Reverse Words in a Sentence (keep case & punctuation same)
# ---------------------------------------------------------------
# Given a string, reverse the words’ order — 
# but remove extra spaces and make sure there is only one space between words.
# Example: "  Python   is  fun!  " → "fun! is Python"


def reverse_words(sentence):
    # Split removes extra spaces by default
    words = sentence.split()
    
    # Reverse the list of words
    reversed_words = ' '.join(reversed(words))
    
    return reversed_words

print(reverse_words("  Python   is  fun!  "))

 


"""
Problem:
Count how many times each character appears in a string.

"""

text = "banana"

char_count = dict(map(lambda c: (c, text.count(c)), set(text)))

print("Character Frequency:")
print(char_count)

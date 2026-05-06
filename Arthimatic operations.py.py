# Assign 1
# Create 4 functions called add, subtract, multiply, divide
# Each function should print the result of the operation
# Ask the user to enter two numbers and the operation (+, -, *, /)
# Call the relavent function based on user input
 
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
def add():
    print(a+b)
def subtraction():
    print(a-b)
def multiply():
    print(a*b)
def divide():
    print(a/b)


add()
subtraction()
multiply()
divide()







# ---------------------------------------------------------------
# 1. Reverse Words in a Sentence (keep case & punctuation same)
# ---------------------------------------------------------------
# Given a string, reverse the words’ order — 
# but remove extra spaces and make sure there is only one space between words.
# Example: "  Python   is  fun!  " → "fun! is Python"



sen = "  python  is  fun  !"
def reverse (sen):
    c = words = sen.split()
   # reversed_words = ' '.join(reversed(words))
print(c)
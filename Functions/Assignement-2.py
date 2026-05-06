#Assign 2
#Create a function called check_even_odd()
#It should take one parameter called 'number'
#It will print 'Even' if the number is even, if not print 'Odd'

a = int(input("Enter a number:"))
def check_even_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("odd")
check_even_odd(a)






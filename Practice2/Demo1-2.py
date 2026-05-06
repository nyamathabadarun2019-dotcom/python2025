choice=int(input('enter your value : '))

def odd_even(a):
    if choice % 2 == 0:
        print(f"{choice} is even number")
    elif choice %2 != 0:
        print(f"{choice} is odd number")
odd_even(choice)
    


def do_addition():
    a = 5
    b = 6
    print(a + b)
do_addition()

a = int(input('Enter first number:'))
b = int(input('Enter second number:'))

def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)

add()
mul()
sub()


def greet(a):
    print(f'Hello {a}')
    print(f'Namaste {a}')

greet('sraven')
greet('deepak')


names = ['sraven', 'arun', 'amar']
def send_loan_reminder(a):
    msg = f'''
    Dear {a},
    Kindly pay your pending dues!


    Thank you
    SBI
    '''
    print(msg)

for names in names:
    send_loan_reminder(names)
    print('============')




names = {'sraven':20000, 'arun':40000, 'amar':25000}
def send_loan_reminder(a,b):
    msg = f'''
    Dear {a},
    Kindly pay your pending dues of Rs,{b}!


    Thank you
    SBI
    '''
    print(msg)

for i in names:
    nmaes = i
    amount = names[i]
    send_loan_reminder(names, amount)
    print('===========================')





cart = []
 
count = 0

while count < 6:

    choice = int(input('Enter 1 to add, 2 to remove: '))

    if choice == 1:

        product = input('Enter product to add:')

        cart.append(product)

    elif choice == 2:

        product = input('Enter product to remove:')

        cart.remove(product)

    count+=1
 
print(cart)
 
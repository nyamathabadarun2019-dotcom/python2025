
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
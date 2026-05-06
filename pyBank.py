balance = 0.0
transactions = []

def deposit(amount):
    global balance


    balance += amount 
    transactions.append(f'Deposited{amount}/-')
    print(f'{amount} deposited successfully')


def withdraw(amount):
    global balance

    if amount > balance:
        print("Insufficent Balance")
    else:
        balance = balance - amount
        transactions.append(f'withdrawn {amount}/-')
        print(f'{amount} withdrawn successfully')




def checkBalance():
    #print(f'Current Balance: {balance}\n')
    #return balance
    print("Current Balance:",balance)



def transactionHistory():
   if not transactions:
    print('No Transaction yet.\n')
   else:
    print('----Transactions History----')
    for t in transactions: 
        print('-',t)
        deposits = sum(1 for t in transactions if 'Deposited' in t)
        withdraws = sum(1 for t in transactions if 'withdrawn' in t)
        print(f'\nTotal Deposits : {deposits}')
        print(f'\nTotal withdraws : {withdraws}')



def menu():
    while True:
        print("----pyBank Menu----")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Exit")



        choice = input('Enter your Choice')
        if choice == '1':
            amount = float(input('Enter your amount to deposit:'))
            deposit(amount)
        elif choice == '2':
             amount = float(input('Enter your amount to withdraw:'))
             withdraw(amount)
        elif choice == '3':
             checkBalance()
        elif choice == '4':
             transactionHistory()
        elif choice == '5':
            print('Thank you for using PyBank. Good bye')
            break
        else:
            print('Invalid choice')

     
menu()
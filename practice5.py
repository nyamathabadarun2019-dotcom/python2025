# Mini ATM Simlator

balance = 1000

while True:
    print("\n1.Check Balance  2.Deposit  3.Withdraw  4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        print("Balance:", balance)
    elif ch == 2:
        amt = int(input("Enter amount: "))
        balance += amt
    elif ch == 3:
        amt = int(input("Withdraw amount: "))
        if amt <= balance:
            balance -= amt
        else:
            print("Insufficient balance")
    elif ch == 4:
        break
    else:
        print("Invalid")
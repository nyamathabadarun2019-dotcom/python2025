# a simple contact book

contacts = {}

while True:
    print("\n1.Add  2.Search  3.View All  4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts[name] = phone
        print("Saved!")
    elif choice == 2:
        name = input("Search name: ")
        print("Phone:", contacts.get(name, "Not found"))
    elif choice == 3:
        print("Contacts:", contacts)
    elif choice == 4:
        break
    else:
        print("Invalid choice")

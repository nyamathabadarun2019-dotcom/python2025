# Assignment 1: Contact Manager
# Create a program that manages a contact list using dictionaries. The program should allow users to:
# Add a new contact with name, phone number, and email
# Update an existing contact
# Delete a contact
# Display all contacts
# Search for a contact by name



# Contact Manager using only dictionary (no if, no loops, no functions)

contacts = {}

# Add Contact
name = input("Enter name to add: ")
phone = input("Enter phone number: ")
email = input("Enter email: ")
contacts[name] = {"phone": phone, "email": email}
print("Contact added:", contacts)

# Update Contact (just overwrites)
name = input("Enter name to update: ")
phone = input("Enter new phone number: ")
email = input("Enter new email: ")
contacts[name] = {"phone": phone, "email": email}
print("After update:", contacts)

# Delete Contact (direct del call)
name = input("Enter name to delete: ")
# You must make sure the name exists, otherwise Python will error
del contacts[name]
print("After delete:", contacts)

# Display All Contacts
print("All contacts:", contacts)

# Search Contact
name = input("Enter name to search: ")
print("Search result:", contacts.get(name))

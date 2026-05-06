"""
Problem:
Create a simple phone book.
Add contacts and search for a contact.

"""

phone_book = {}

phone_book.update({
    "Shiva": 9876543210,
    "Rahul": 9123456789
})

print("Searching for Shiva:")
print(phone_book.get("Shiva", "Contact not found"))

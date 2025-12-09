# password strength checker

password = input("Enter password: ")

length = len(password) >= 8
upper = any(ch.isupper() for ch in password)
lower = any(ch.islower() for ch in password)
digit = any(ch.isdigit() for ch in password)
special = any(ch in "!@#$%^&*()" for ch in password)

if length and upper and lower and digit and special:
    print("Strong Password")
else:
    print("Weak Password")
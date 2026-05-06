# Stored correct password
correct_password = "python123"

# Ask user to enter password
user_password = input("Enter your password: ")

# Check password
if user_password == correct_password:
    print("✅ Password is correct. Access granted.")
else:
    print("❌ Incorrect password. Access denied.")

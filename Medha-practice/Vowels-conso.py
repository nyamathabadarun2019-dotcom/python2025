user = input("enter the input:")
vowels1 = user.count("a")
vowels2 = user.count("e")
vowels3 = user.count("i")
vowels4 = user.count("o")
vowels5 = user.count("u")
total_vowels = vowels1 + vowels2 + vowels3 + vowels4 + vowels5
total_letters =len(user)
total_consonants = total_letters -total_vowels
print(f"vowels present:{total_vowels}")
print(f"consonants present :{total_consonants}")



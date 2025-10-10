
#Assign 4
#Ask the user for a number
#Create a function called generate_table(number)
# It should take 'number' as param and print multiplication table from 1 to 10 for this number
#Call the function

num = int(input("Enter a number:"))
def generate_table(number):
    for i in range(1,11):
        print(f"{number} x {i} = {number*i}")


generate_table(number = num)         
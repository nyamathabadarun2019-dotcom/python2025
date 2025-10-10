 
#Assign 3
#Ask for student name, and grade
#Create a function display_student_info(name, grade)
#It should print output as below
## Name: Ravi
## Grade: A



name = input("Enter student name:")
grade = input("Enter student grade:")
def display_student_info(name,grade):
    print(f"Name:  {name}")
    print(f"Grade: { grade}")

display_student_info(name,grade)    
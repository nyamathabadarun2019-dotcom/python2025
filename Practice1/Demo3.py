"""
Problem:
Create a dictionary of student names and marks.
Display only students who scored more than 50.

"""

students = {
    "Ravi": 65,
    "Sita": 45,
    "Arjun": 78,
    "Neha": 40
}

passed_students = dict(filter(lambda item: item[1] > 50, students.items()))

print("Students who scored more than 50:")
print(passed_students)

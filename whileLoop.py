all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

"""
You are adding students to a Poetry class, the size of which is capped at 6. 
While the length of the students_in_poetry list is less than 6, use .pop() to take a student off 
the all_students list and add it to the students_in_poetry list.
"""
size = 6
while (len(students_in_poetry) < size):
    popped_student = all_students.pop()
    students_in_poetry.append(popped_student)
print(students_in_poetry)


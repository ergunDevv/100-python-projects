import random
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

students_score = {student: random.randint(0, 100) for student in names}
print(students_score)
passed_students = {student: students_score[student]
                   for student in students_score if students_score[student] > 50}
print(passed_students)

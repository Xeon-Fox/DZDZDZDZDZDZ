from functools import reduce

students = (
    {"name": "Alex", "age": 20, "course": "Python", "average_grade": 4.5},
    {"name": "Jane", "age": 22, "course": "Python", "average_grade": 4.7},
    {"name": "John", "age": 21, "course": "Java", "average_grade": 4.2},
)

total_age = reduce(lambda acc, student: acc + student["age"], students, 0)
average_age = total_age / len(students)

python_students = [student for student in students if student["course"] == "Python"]
if python_students:
    total_grade = reduce(lambda acc, student: acc + student["average_grade"], python_students, 0)
    average_grade = total_grade / len(python_students)
else:
    average_grade = None

print("Средний возраст:", average_age)
print("Средний бал:", average_grade)

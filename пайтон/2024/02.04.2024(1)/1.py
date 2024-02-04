students_tuple = ({'name': 'Alex Novak', 'age': 21, 'course': 'Python', 'average_grade': 9.78},{'name': 'Jane Doe', 'age': 18, 'course': 'PHP', 'average_grade': 9.2}, {'name': 'John Doe', 'age': 20, 'course': 'HTML', 'average_grade': 7}
)

names_tuple = tuple(map(lambda student: student['name'], students_tuple))

print(names_tuple)
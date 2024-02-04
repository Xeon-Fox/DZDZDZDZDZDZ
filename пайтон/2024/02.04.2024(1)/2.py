students_tuple = ({'name': 'Alex Novak', 'age': 17, 'course': 'Python', 'average_grade': 11}, {'name': 'Jane Doe', 'age': 16, 'course': 'HTML', 'average_grade': 12}, {'name': 'John Doe', 'age': 15, 'course': 'HTML', 'average_grade': 12}, {'name': 'Johnson Baby', 'age': 21, 'course': 'Python', 'average_grade': 11})
html_students_tuple = tuple(filter(lambda student: student['course'] == 'Html', students_tuple))
top_students_tuple = tuple(filter(lambda student: student['average_grade'] > 11, students_tuple))

print("HTML:", html_students_tuple)
print("Топ студенты:", top_students_tuple)

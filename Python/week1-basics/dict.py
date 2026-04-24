student = {'name': 'John', 'age': 25, 'courses': ['Math', 'Science']}
print(student)
print(student['name'])
print(student['courses'])

print(student.get('name'))
print(student.get('phone','Not Found'))

student['phone'] = '555-5555'
student['name'] = 'Jane'

print(student)

student.update({'name': 'John', 'age': 26, 'email': 'john@example.com'})

print(student)

del student['age']
print(student)

email = student.pop('email')
print(student)
print(email)

print(len(student))
print(student.keys())
print(student.values())

print(student.items())

for key, value in student.items():
    print(key, value)
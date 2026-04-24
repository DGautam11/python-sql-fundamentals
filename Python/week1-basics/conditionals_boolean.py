language = 'Java'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
elif language == 'JavaScript':
    print('Language is JavaScript')
else:    
    print('No match')


user = 'Admin'
logged_in = False

if user=='Admin' and logged_in:
    print('Admin page')
else:
    print('Bad credentials')

if not logged_in:
    print('Please log in')

a = [1,2,3]
b = [1,2,3]

print(a == b)
print(id(a))
print(id(b))
print(a is b)

c = a
print(id(a))
print(id(c))
print(a is c)

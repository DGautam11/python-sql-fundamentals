message = "Hello, World!"
print(message)
print(len(message))
print(message[0])
print(message[12])
print(message[:5])
print(message[7:])
print(message.lower())
print(message.upper())
print(message.count("o"))
print(message.find("Hello"))
print(message.replace("World", "Python"))
greeting = "Hello"
name = "Alice"

greeting_message =  greeting + ', ' + name 
print(greeting_message)

greeting_message = '{}, {},Welcome to Python!'.format(greeting, name)
print(greeting_message)

greeting_message = f'{greeting}, {name.upper()}, Welcome to Python!'
print(greeting_message)

num = 3

print(type(num))
print(num % 2)
print(num ** 2)

num += 1
print(num)
print(abs(-5))
print(round(3.75))
print(round(3.75, 1))

num_1 = 3
num_2 = 4
print(num_1 == num_2)
print(num_1 != num_2)
print(num_1 <= num_2)

num_3 = '100'
num_4 = '200'

num_3 = int(num_3)
num_4 = int(num_4)

print(num_3 + num_4)

name = 'ada lovelace'
print(name.title())
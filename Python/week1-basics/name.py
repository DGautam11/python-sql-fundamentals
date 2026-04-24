name = 'ada lovelace'
print(name.title())

print(name.upper())
print(name.lower())

first_name ='ada'
last_name = 'lovelace'
full_name = f"{first_name} {last_name}"
print(full_name)
message = f"Hello, {name.title()}!"
print(message)


print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Stripping whitespace

favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(favorite_language)

last_name  = '  Lovelace'
last_name = last_name.lstrip()
print(last_name)

#Removing prefixes

nostarch_url = 'https://www.nostarch.com'
simple_url = nostarch_url.removeprefix('https://')
print(simple_url)

#TRY IT YOURSELF
name = 'Deepan GTM'
print(f'Hello, {name} Learning Python again in 2026!')

print(name.lower())
print(name.upper())
print(name.title())

print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')

famous_person = 'Albert Einstein'
message = f'{famous_person} once said, "A person who never made a mistake never tried anything new."'
print(message)

name = '  Deepan GTM  '
print(name.lstrip())
print(name.rstrip())
print(name.strip())

file_name = 'python_basics.txt'
print(file_name.removesuffix('.txt'))
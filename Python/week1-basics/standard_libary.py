from my_module import find_index, test
import sys
import random
import math
import datetime
import calendar
import os

courses = ['History','Math','Physics','CompSci ']

index = find_index(courses, 'History')
print(index)
print(test)

print(sys.path)
print(random.choice(courses))

rads = math.radians(90)
print(rads)
print(math.sin(rads))

today = datetime.date.today()
print(today)

print(calendar.isleap(2020))

print(os.getcwd())
print(os.__file__)
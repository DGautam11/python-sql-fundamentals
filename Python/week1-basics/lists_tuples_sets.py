courses = ['History','Math','Physics','CompSci ']
print(courses)
print(len(courses))
print(courses[0])
print(courses[-1])
print(courses[0:2])
print(courses[2:])
courses.append('Art')
print(courses)
courses.insert(0, 'Education')
print(courses)

courses_2 = ['Design','Programming']
courses.insert(0, courses_2)
print(courses)
print(courses[0])

courses = ['History','Math','Physics','CompSci ']
courses_2 = ['Design','Programming']
courses.extend(courses_2)

courses.remove('Math')
popped_item = courses.pop()
print(courses)
print(f"Popped item: {popped_item}")

courses.reverse()
print(courses)

courses.sort()
print(courses)

nums = [11,3,44,21,42,8]
nums.sort(reverse=True)
print(nums)

courses = ['History','Math','Physics','CompSci ']
sorted_courses = sorted(courses)
print(courses)
print(sorted_courses)

print(min(nums))
print(max(nums))
print(sum(nums))

print(courses.index('CompSci '))
print('Math' in courses)

for item in courses:
    print(item)

for index, course in enumerate(courses, start=1):
    print(index, course)

course_str = ', '.join(courses)
print(course_str)

new_list = course_str.split(', ')
print(new_list)

#TUPLES
tuple_1 = ('History','Math','Physics','CompSci ')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)



#SETS
cs_courses = {'History','Math','Physics','CompSci ','Math'}
print(cs_courses)
print('Math' in cs_courses)
art_courses = {'History','Math','Art','Design'}
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))

print(cs_courses.union(art_courses))

empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = set()
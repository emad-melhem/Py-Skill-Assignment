        # 1
coordinates = (34.0522, -118.2437)
for item in coordinates:
    print(item)

        # 2
student = {'name': 'Alice', 'age': 24, 'courses': ['Math', 'Science', 'English']}
student.update({'graduated': False}) # add a new dictionary.
student['age'] = 25 # Modified the value of 'age' key.
print(student)

        # 3
unique_numbers = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
unique_numbers.add(6) # add an item into set.
unique_numbers.remove(2) # remove item from set.
print(unique_numbers)
print(3 in unique_numbers) # check if 3 in the set.
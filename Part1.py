          # Task 1
          # 1
x = 25
y = 3.13
z = "Advanced Python"
is_active = False

        # 2
# I added formatting to the numbers to make the output clearer.
print("{:.2f}".format(x / y))
print(str(x) + z)
 # Or
 # print(str(x), z, sep="")
is_active = not is_active
print(is_active)

print("------------")

        # Task 2
        # 1
text = "Python programming is powerful and versatile."
print(text[7:18])

        # 2
split_text = text.split(" ")
print("-".join(split_text))

        # 3
numbers = list(range(10, 101, 10))
squares = [i ** 2 for i in numbers]
""" OR
squares = []
for number in numbers:
    squares.append(number ** 2)
"""
print(squares)

print("------------")

        # Task 3
        # 1
coordinates = (34.0522, -118.2437)
for item in coordinates:
    print(item)

        # 2
student = {'name': 'Alice', 'age': 24, 'courses': ['Math', 'Science', 'English']}
student.update({'graduated': False})
student['age'] = 25
print(student)

        # 3
unique_numbers = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
unique_numbers.add(6)
unique_numbers.remove(2)
print(3 in unique_numbers)

print("------------")

        # Task 4
        # 1
def is_prime(n):
    lst = [2, 3, 5, 7]
    for item in lst:
        if (n == 1) or (n not in lst and n % item == 0):
            return False
    return True
 # I created a list to make the numbers on the screen appear clearer.
lst_prime_numbers = []
for number in range(1, 51):
    if is_prime(number):
        lst_prime_numbers.append(number)
print(lst_prime_numbers)

        # 2
list_numbers = list(range(1, 16))
 # I created a list to make the numbers on the screen appear clearer.
list_results = []
for number in list_numbers:
    print_string = ""
    if number % 3 == 0:
        print_string += "Fizz"
    if number % 5 == 0:
        print_string += "Buzz"
    if not print_string:
        list_results.append(number)
    else:
        list_results.append(print_string)
print(list_results)
          # Task 1
          # 1
x = 25
y = 3.13
z = "Advanced Python"
is_active = False

        # 2
# I added formatting to the numbers to make the output clearer.
print("{:.2f}".format(x / y))
new_string = str(x) + z
 # OR
 # new_string = "".join([str(x), z])
print(new_string)
 #OR
 # print(f"{x}{z}")
 #OR
 # print(x, z, sep="")
is_active = not is_active # toggle the bool variable.
print(is_active)

print("------------")

        # Task 2
        # 1
text = "Python programming is powerful and versatile."
#       01234567          18
print(text[7:18]) # slicing from index 0 to 18 except index 18 with step =1.

        # 2
        
split_text = text.split(" ") # split the text to list of words without space
print("-".join(split_text)) # join the list with '-'

        # 3
numbers = list(range(10, 101, 10)) # creat list numbers 10-100 with step 10
squares = [i ** 2 for i in numbers] # the shortcut method to creat new list with square.
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
student.update({'graduated': False}) # add a new dictionary.
student['age'] = 25 # Modified the value of 'age' key.
print(student)

        # 3
unique_numbers = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
unique_numbers.add(6) # add an item into set.
unique_numbers.remove(2) # remove item from set.
print(3 in unique_numbers) # output is true.

print("------------")

        # Task 4
        # 1
def is_prime(n):
    lst = [2, 3, 5, 7]
    for item in lst:
        #return false if n=1 or n is divisible by one of (2, 3, 5, 7) and not in it.
        if (n == 1) or (n not in lst and n % item == 0):
            return False
    return True # if n is prime

 # I created a list to make the numbers on the screen appear clearer.
lst_prime_numbers = []
for number in range(1, 51):
    if is_prime(number): # detect if number is prime
        lst_prime_numbers.append(number) # i can use here print(number)
print(lst_prime_numbers)

        # 2
list_numbers = list(range(1, 16)) # creat list [1..15]
 # I created a list to make the numbers on the screen appear clearer.
list_results = []
for number in list_numbers:
    print_string = ""
    if number % 3 == 0:
        print_string += "Fizz"
    if number % 5 == 0:
        print_string += "Buzz"
    if not print_string:
        list_results.append(number) # i can use here print(number)
    else:
        list_results.append(print_string)# i can use here print(print_string)
print(list_results)

print("------------")
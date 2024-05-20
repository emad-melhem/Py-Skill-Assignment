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
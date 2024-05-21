        # 1
def is_prime(n):
    if n <= 1: # if number is less or equal than 1 return false
        return False
    for i in range(2, int(n**0.5) + 1): #check all number between 2 and the square root of number
        if n % i == 0:
            return False
    return True # return true if n is not divisible by numbers

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
    if number % 3 == 0 and number % 5 == 0:
        list_results.append("FizzBuzz")
    elif number % 3 == 0:
        list_results.append("Fizz")
    elif number % 5 == 0:
        list_results.append("Buzz")
    else:
        list_results.append(number)
        
print(list_results)
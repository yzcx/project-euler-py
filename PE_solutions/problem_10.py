
# Project Euler problem 10

def prime(num):
    for i in range(2, int((num**0.5))+1): # Divisors only up to square root of number
        if not num % i: # Checking for perfect divisor
            return False
    return True

result = 2 # Allows us to skip all even numbers

for i in range(3, 2000000, 2): # Iterating through odd numbers from 3 to 2mil
    if prime(i):
        result += i

print(result)
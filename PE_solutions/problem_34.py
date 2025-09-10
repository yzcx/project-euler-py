
# Project Euler problem 34: digit factorials

import math

factorials = [math.factorial(i) for i in range(10)] # Calculating factorial for each digit to save time

limit = 2903040
total_sum = 0

for n in range(3, limit):
    digit_factorial_sum = 0
    temp_n = n
    while temp_n > 0:
        digit = temp_n % 10
        digit_factorial_sum += factorials[digit]
        temp_n //= 10
    if n == digit_factorial_sum:
        total_sum += n

print(total_sum)
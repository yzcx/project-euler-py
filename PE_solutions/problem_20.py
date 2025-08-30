
# Project Euler problem 20

import math

factorial = math.factorial(100)
factorial_str = str(factorial)
digit_sum = sum(int(digit) for digit in factorial_str)

print(digit_sum)
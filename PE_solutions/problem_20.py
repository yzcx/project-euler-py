
# Project Euler problem 20: factorial digit sum

import math

factorial = math.factorial(100)
factorial_str = str(factorial)
digit_sum = sum(int(digit) for digit in factorial_str)

print(digit_sum)
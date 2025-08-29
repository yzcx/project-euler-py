
# Project Euler problem 12

from sympy import divisors

i = 1
while True:
    triangle = sum(range(1, i+1))
    i += 1
    if len(divisors(triangle)) > 500:
        print(triangle)
        break
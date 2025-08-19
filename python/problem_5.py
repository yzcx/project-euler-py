
# Project Euler problem 5

import math

number = 1

for i in range(1, 21):
    number = math.lcm(number, i) # Calculating LCM by iterating through range

    print(number)
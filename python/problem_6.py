
# Project Euler problem 6

sum_of_squares = 0
sum_of_numbers = 0

for i in range(1, 101):
    sum_of_squares += i ** 2 # Calculates square of current number and adds to first total
    sum_of_numbers += i # Adds current number to second total
square_of_sum = sum_of_numbers ** 2 # Squaring total sum of numbers

difference = square_of_sum - sum_of_squares
print(difference)
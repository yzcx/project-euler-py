
# Project Euler problem 2: even fibonacci numbers

total = 2 # The first even term
first = 1
second = 2

while True:
    fibonacci = first + second
    first = second
    second = fibonacci # For the next iterations
    if fibonacci > 4000000:
        break

    if fibonacci % 2 == 0:
        total += fibonacci

print(total)
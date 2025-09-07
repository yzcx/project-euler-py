
# Project Euler problem 25: 1000 digit Fibonacci number

import itertools

def compute():
    DIGITS = 1000
    prev = 1
    cur = 0
    for i in itertools.count(): # I use an infinite counter to keep track of index of each number
        if len(str(cur)) > DIGITS: # Checking if current length of number is equal to target
            raise RuntimeError("Not found")
        elif len(str(cur)) == DIGITS:
            return str(i)

        prev, cur = cur, prev + cur

if __name__ == "__main__":
    print(compute())
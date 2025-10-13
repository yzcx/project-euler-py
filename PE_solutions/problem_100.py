
# Project Euler problem 100: arranged probability

import math

def compute():
    x0 = 3 # Solution to Pell equation
    y0 = 1
    x = x0
    y = y0

    while True: # Generates successive solutions to the Pell equation
        sqrt = math.isqrt(y ** 2 * 8 + 1)
        if sqrt % 2 == 1:  # Is odd
            blue = (sqrt + 1) // 2 + y
            if blue + y > 10 ** 12:
                return str(blue)

        nextx = x * x0 + y * y0 * 8 # Generates next solution using recurrence relation
        nexty = x * y0 + y * x0
        x = nextx
        y = nexty

if __name__ == "__main__":
    print(compute())
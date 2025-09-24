
# Project Euler problem 62: cubic permutations

import itertools

def compute():
    numdigits = 0
    data = {}
    for i in itertools.count(): # Checking cubes of consecutive integers
        digits = [int(c) for c in str(i ** 3)]
        digits.sort()
        numclass = "".join(str(d) for d in digits)

        if len(numclass) > numdigits: # When a cube has more digits than the previous ones, it means we have found all permutations for previous number of digits
            candidates = [lowest for (lowest, count) in data.values() if count == 5]
            if len(candidates) > 0:
                return str(min(candidates) ** 3)
            data = {}
            numdigits = len(numclass)

        lowest, count = data.get(numclass, (i, 0))
        data[numclass] = (lowest, count + 1)

if __name__ == "__main__":
    print(compute())
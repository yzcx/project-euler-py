
# Project Euler problem 61: cyclical figurate numbers

import itertools

def compute():
    numbers = [[set() for j in range(100)] for i in range(9)]
    for sides in range(3, 9):
        for n in itertools.count(1):
            num = figurate_number(sides, n)
            if num >= 10000:
                break
            if num >= 1000:
                numbers[sides][num // 100].add(num)

    def find_solution_sum(begin, current, sidesused, sum): # Recursive function searching for cyclic chain of 6 numbers
        if sidesused == 0b111111000:
            if current % 100 == begin // 100:
                return sum
        else:
            for sides in range(4, 9): # Tries to find the next number in the chain, iterate through unused figurate types
                if (sidesused >> sides) & 1 != 0:
                    continue
                for num in numbers[sides][current % 100]:
                    temp = find_solution_sum(begin, num, sidesused | (1 << sides), sum + num)
                    if temp is not None:
                        return temp
            return None

    for i in range(10, 100): # Start search with 4 digit triangle number, bitmask is initialised to show only triangle side is 1 < 3
        for num in numbers[3][i]:
            temp = find_solution_sum(num, num, 1 << 3, num)
            if temp is not None:
                return str(temp)
    raise AssertionError("No solution")

def figurate_number(sides, n): # Calculates figurate number based on side and index
    return n * ((sides - 2) * n - (sides - 4)) // 2

if __name__ == "__main__":
    print(compute())
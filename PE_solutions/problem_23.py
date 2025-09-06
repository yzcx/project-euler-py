
# Project Euler problem: non-abundant sums

def compute():
    LIMIT = 28124 # Problem's UB is 28124 so I set my limit as that to be safe
    divisorsum = [0] * LIMIT # Creating a list to store the sum of divisors
    for i in range(1, LIMIT):
        for j in range(i * 2, LIMIT, i):
            divisorsum[j] += i
    abundantnums = [i for (i, x) in enumerate(divisorsum) if x > i]

    expressible = [False] * LIMIT # Creating a list to keep track of every number that can be expressed as a sum of two abundant numbers, I make them false
    for i in abundantnums:
        for j in abundantnums:
            if i + j < LIMIT:
                expressible[i + j] = True
            else:
                break

    ans = sum(i for (i, x) in enumerate(expressible) if not x) # Finding the sum of numbers that cannot be expressed
    return str(ans)

if __name__ == "__main__":
    print(compute())
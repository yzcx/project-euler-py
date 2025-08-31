
# Project Euler problem 21: amicable numbers

def findSumOfDivisors(num): # Finding sum of proper divisors by only checking square root of number
    # If I find divisor I know that num / f is also a divisor which is more efficient to get pairs
    if num <= 1:
        return 0

    sum = 1
    for f in range(2, int(num ** 0.5) + 1):
        if num % f == 0:
            sum += f
            if f != num // f:
                sum += num // f
    return sum

limit = 10000
sumAmicables = 0

numToDivisorSum = {n: findSumOfDivisors(n) for n in range(1, limit)} # Calulating and storing sum of divisors first so when I check for pairs I don't have to recalculate

for n in range(1, limit):
    divisorSum = numToDivisorSum[n]

    if divisorSum < limit and numToDivisorSum.get(divisorSum) == n and divisorSum != n: # Prevents numbers from being its own pair
        sumAmicables += n

print(sumAmicables)
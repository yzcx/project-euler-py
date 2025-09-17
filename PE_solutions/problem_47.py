
# Project Euler problem 47: distinct primes factors

import functools, itertools, math

def compute(): # Checking numbers one by one until I find number that fits criteria. Lambda function checks if number i and next 3 numbers all have 4 distinct prime factors
	cond = lambda i: all((count_distinct_prime_factors(i + j) == 4) for j in range(4))
	ans = next(filter(cond, itertools.count()))
	return str(ans)

@functools.cache
def count_distinct_prime_factors(n): # Efficiently counting prime numbers. Using cache to store results so I don't have to recalculate numbers if they same number appears again
	count = 0
	while n > 1:
		count += 1
		for i in range(2, math.isqrt(n) + 1):
			if n % i == 0:
				while True:
					n //= i
					if n % i != 0:
						break
				break
		else:
			break
	return count

if __name__ == "__main__":
	print(compute())
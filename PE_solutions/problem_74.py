
# Project Euler problem 74: digit factorial chains

import math

def compute():
	LIMIT = 10**6
	ans = sum(1 for i in range(LIMIT) if get_chain_length(i) == 60) # Sum of starting numbers that result in a chain length of 60
	return str(ans)

def get_chain_length(n):
	seen = set() # Tracks number in chain to detect a cycle
	while True:
		seen.add(n)
		n = factorialize(n)
		if n in seen:
			return len(seen)

def factorialize(n): # Calculates next term by summing factorials of digits of n
	result = 0
	while n != 0:
		result += FACTORIAL[n % 10]
		n //= 10
	return result

FACTORIAL = [math.factorial(i) for i in range(10)] # Pre calculates factorial of digits 0 through 9

if __name__ == "__main__":
	print(compute())
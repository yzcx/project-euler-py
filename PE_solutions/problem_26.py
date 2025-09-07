
# Project Euler problem 26: reciprocal cycles

import itertools

def compute(): # Using a helper function to check every number from 1 to 1000 and find the one that gives the longest cycle
	ans = max(range(1, 1000), key=reciprocal_cycle_len)
	return str(ans)

def reciprocal_cycle_len(n): # Calculates the length of the repeating cycle for a given number
	seen = {}
	x = 1
	for i in itertools.count(): # Long division
		if x in seen:
			return i - seen[x]
		else:
			seen[x] = i
			x = x * 10 % n

if __name__ == "__main__":
	print(compute())
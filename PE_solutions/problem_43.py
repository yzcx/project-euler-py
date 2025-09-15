
# Project Euler problem 43:sub-string divisibility

import itertools

def compute():
	ans = sum(int("".join(map(str, num)))
		for num in itertools.permutations(list(range(10)))
		if is_substring_divisible(num))
	return str(ans)

DIVISIBILITY_TESTS = [2, 3, 5, 7, 11, 13, 17] # Prime numbers we need to check against

def is_substring_divisible(num): # Checks if number follows divisibility rules
	return all((num[i + 1] * 100 + num[i + 2] * 10 + num[i + 3]) % p == 0 # Using all to check if true all at once
		for (i, p) in enumerate(DIVISIBILITY_TESTS))

if __name__ == "__main__":
	print(compute())

# Project Euler problem 52: permuted multiples

import itertools

def compute():
	cond = lambda i: all(sorted(str(i)) == sorted(str(j * i)) for j in range(2, 7)) # Checks if i and multiples all have same digits
	ans = next(i for i in itertools.count(1) if cond(i))
	return str(ans)

if __name__ == "__main__":
	print(compute())
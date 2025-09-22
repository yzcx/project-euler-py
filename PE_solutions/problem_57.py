
# Project Euler problem 57: square root convergents

def compute(): # I loop 1000 times to get all the fractions
	LIMIT = 1000
	ans = 0
	numer = 0 # Initialising num. and denom. for recurrence relation
	denom = 1
	for _ in range(LIMIT): # For loop for 1000 expansions
		numer, denom = denom, denom * 2 + numer
		if len(str(numer + denom)) > len(str(denom)): # Checking if num. of full expansion has more digits than the denom.
			ans += 1
	return str(ans)

if __name__ == "__main__":
	print(compute())
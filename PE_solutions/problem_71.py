
# Project Euler problem 71: ordered fractions

def compute():
	LIMIT = 1000000
	maxnumer = 0
	maxdenom = 1
	for d in range(1, LIMIT + 1): # Iterate through every possible denom. up to limit
		n = d * 3 // 7

		if d % 7 == 0: # If d is multiple of 7 then n/d equals 3/7
			n -= 1

		if n * maxdenom > d * maxnumer: # Compare fraction n/d with best fraction found ( max numer. / max denom. )
			maxnumer = n
			maxdenom = d
	return str(maxnumer)

if __name__ == "__main__":
	print(compute())
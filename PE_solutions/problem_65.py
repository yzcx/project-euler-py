
# Project Euler problem 65: convergents of e

def compute():
	numer = 1
	denom = 0
	for i in reversed(range(100)): # Iterate backward from 100th to 1st term
		numer, denom = e_contfrac_term(i) * numer + denom, numer
	ans = sum(int(c) for c in str(numer)) # Converting it to string and sum its digits
	return str(ans)

def e_contfrac_term(i): # Returns coefficient for continued fraction of 'e'
	if i == 0:
		return 2
	elif i % 3 == 2:
		return i // 3 * 2 + 2
	else:
		return 1

if __name__ == "__main__":
	print(compute())
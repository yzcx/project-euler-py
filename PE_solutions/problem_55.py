
# Project Euler problem 55: lychrel numbers

def compute():
	ans = sum(1 for i in range(10000) if is_lychrel(i))
	return str(ans)

def is_lychrel(n):
	for i in range(50): # Perform reverse and add process up to 50 times
		n += int(str(n)[ : : -1]) # Reverse no. and add to original
		if str(n) == str(n)[ : : -1]: # Check if new no. is a palindrome
			return False
	return True

if __name__ == "__main__":
	print(compute())
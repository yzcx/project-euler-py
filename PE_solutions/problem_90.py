
# Project Euler problem 90: cube digit pairs

def popcount(n): # Helper function to count num. of set bits
    return bin(n).count('1')

SQUARES = [(i ** 2 // 10, i ** 2 % 10) for i in range(1, 10)]

def test_bit(x, i):
    return ((x >> i) & 1) != 0

def is_arrangement_valid(a, b):

    if test_bit(a, 6) or test_bit(a, 9): # Interchangeability rule - if a die has a 6 or 9 it cant represent both.
        a |= (1 << 6) | (1 << 9)
    if test_bit(b, 6) or test_bit(b, 9):
        b |= (1 << 6) | (1 << 9)
    return all(((test_bit(a, c) and test_bit(b, d)) or (test_bit(a, d) and test_bit(b, c))) # Validation check
               for (c, d) in SQUARES)

def compute(): # Brute force check
    ans = sum(1
              for i in range(1 << 10)
              for j in range(i, 1 << 10)
              if popcount(i) == popcount(j) == 6 and is_arrangement_valid(i, j))
    return str(ans)

if __name__ == "__main__":
    print(compute())
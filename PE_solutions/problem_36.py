
# Project Euler problem 36: double-base palindromes

def is_palindrome(s):
    return s == s[::-1]

def solve():
    total_sum = 0
    for n in range(1, 1000000, 2): # Only need to check odd numbers because base 2 palindrome must end in 1
        if is_palindrome(str(n)) and is_palindrome(bin(n)[2:]): # Checking if number is in base 10 and base 2
            total_sum += n
    return total_sum

if __name__ == "__main__":
    result = solve()
    print(result)

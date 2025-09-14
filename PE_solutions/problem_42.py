
# Project Euler problem 42: coded triangle numbers

def solve():
    with open('p42.txt', 'r') as f:
        words = [word.strip('"') for word in f.read().split(',')]

    max_word_value = 16 * 26 # Safe UB for calculation

    triangle_numbers = set() # Pre calculating triangle numbers up to max for fast lookups
    n = 1
    tn = 1
    while tn <= max_word_value:
        triangle_numbers.add(tn)
        n += 1
        tn = n * (n + 1) // 2

    triangle_word_count = 0
    for word in words:
        word_value = sum(ord(char) - ord('A') + 1 for char in word)
        if word_value in triangle_numbers:
            triangle_word_count += 1
    return str(triangle_word_count)

if __name__ == "__main__":
    print(solve())
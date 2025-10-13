
# Project Euler problem 98: anagramic squares

import math
import re

def is_square(n):
    if n < 0:
        return False
    root = math.isqrt(n)
    return root * root == n

def max_square_pair(a, b, i, A, U): # Recursive function to check every unique digit assignment and find max square
    if i == len(a):
        if (a[0] in A and A[a[0]] == 0) or (b[0] in A and A[b[0]] == 0):
            return 0
        n_a, n_b = 0, 0
        for x, y in zip(a, b):
            n_a = n_a * 10 + A[x]
            n_b = n_b * 10 + A[y]
        if is_square(n_a) and is_square(n_b):
            return max(n_a, n_b)
        else:
            return 0
    elif a[i] in A: # Pruning, if the current letter has already been assigned digit
        return max_square_pair(a, b, i + 1, A, U)
    else: # Recursive step, try assigning every available digit to current unassigned letter
        res = 0
        for d in range(10):
            if not U[d]:
                U[d] = True
                A[a[i]] = d
                res = max(max_square_pair(a, b, i + 1, A, U), res)
                del A[a[i]]
                U[d] = False
        return res

def compute():
    with open("p98.txt", 'r') as f:
        content = f.read().strip()
        WORDS = [w.strip('"') for w in re.split(r'[",]+', content) if w.strip('"')]

    anagrams = {}
    for word in WORDS:
        key = "".join(sorted(word))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(word)

    ans = 0 # Iterate through all unique anagram pairs and find max square
    for words in anagrams.values():
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                assignments = {}
                ans = max(max_square_pair(words[i], words[j], 0, assignments, [False] * 10), ans)
    return str(ans)

if __name__ == "__main__":
    print(compute())
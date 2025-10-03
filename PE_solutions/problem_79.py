# Project Euler problem 79: passcode derivation

import itertools

def is_subsequence(sub, main): # Checks if sequence of characters in sub appears in main in correct order
    i = 0
    j = 0
    while i < len(sub) and j < len(main):
        if sub[i] == main[j]:
            i += 1
        j += 1
    return i == len(sub)

def compute():
    with open("p79.txt", 'r') as f:
        SAMPLES = [line.strip() for line in f if line.strip()]

    chars_set = set("".join(SAMPLES)) # Determines unique digits that must be in passcode
    charsed = sorted(list(chars_set))

    for guess_tuple in itertools.permutations(charsed): # Brute force check all permutations of unique digits
        guess = "".join(guess_tuple)

        if all(is_subsequence(s, guess) for s in SAMPLES): # Check if every login attempt is valid subsequence of current guess
            return guess

if __name__ == "__main__":
    print(compute())
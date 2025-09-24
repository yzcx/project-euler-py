
# Project Euler problem 59: XOR decryption

def compute():
    with open("p59.txt", "r") as f:
        ciphertext_str = f.read().strip()
        ciphertext = [int(n) for n in ciphertext_str.replace(" ", "").split(',')]

    bestkey = max(((x, y, z) # Iterating through all possible 3 characters lowercase keys, finds the key that gives the highest score when decrypted
                   for x in range(97, 123)
                   for y in range(97, 123)
                   for z in range(97, 123)),
                  key=lambda key: get_score(decrypt(ciphertext, key)))

    ans = sum(decrypt(ciphertext, bestkey)) # Decrypts text with best key and finds sum of all ASCII values
    return str(ans)

def get_score(plaintext): # Scores how "good" a decrypted message is, a higher score means it is more likely to be readable
    result = 0
    for c in plaintext:
        if 65 <= c <= 90:
            result += 1
        elif 97 <= c <= 122:
            result += 2
        elif c < 0x20 or c == 0x7F:
            result -= 10
    return result

def decrypt(ciphertext, key): # Decrypts ciphertext with given key. Uses XOR operation with a repeating key
    return [(c ^ key[i % len(key)]) for (i, c) in enumerate(ciphertext)]

if __name__ == "__main__":
    print(compute())
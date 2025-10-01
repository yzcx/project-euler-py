
# Project Euler problem 75: singular integer right triangles

import math

def compute():
    LIMIT = 1500000

    triples = set()

    for s in range(3, math.isqrt(LIMIT) + 1, 2): # Iterate through possible s values for Euclid's formula variant
        for t in range(s - 2, 0, -2): # Iterate through possible t values
            if math.gcd(s, t) == 1: # Check for coprimality and ensure triple is primitive
                a = s * t
                b = (s * s - t * t) // 2
                c = (s * s + t * t) // 2
                if a + b + c <= LIMIT:
                    triples.add((a, b, c))

    ways = [0] * (LIMIT + 1) # Array counting unique right triangles and how many correspond to each perimeter L

    for triple in triples: # Iterate through triples
        sigma = sum(triple)
        for i in range(sigma, len(ways), sigma):
            ways[i] += 1

    ans = ways.count(1)
    return str(ans)

if __name__ == "__main__":
    print(compute())
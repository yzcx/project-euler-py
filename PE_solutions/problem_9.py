
# Project Euler problem 9

for c in range(334,500): # I know that 'c' is greater than 1000/3 and less than 500 due to triangle's rule
    for a in range(1, int((1000-c)/2)): # Looping through 'a' possible values, since a < b is less than half or remaining sum (1000 - c)
        b = (1000 - c) - a
        if b > a:
            if a**2 + b**2 == c**2: # Testing triplet to see if it satisfies Pythagorean theorem
                print(a*b*c)
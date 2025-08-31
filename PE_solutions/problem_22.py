
# Project Euler problem 22: names scores

alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

f = open("p22.txt", "r")
names = f.read().split(",")
f.close()

names.sort()

total = 0
position = 1

for name in names: # Looping through each name in sorted list
    name = name.strip('"')
    score = 0
    for letter in [*name]: # Using lookup string to find alphabet
        score += alphabet.index(letter)
    total += score * position
    position += 1

print(total)
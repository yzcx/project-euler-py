
# Project Euler problem 77: coin partitions

import itertools

MODULUS = 10 ** 6

def compute():

    partitions = [1] # DP array

    for i in itertools.count(len(partitions)): # Iterate through n to calculate p until solution is found
        item = 0
        for j in itertools.count(1):
            sign = -1 if j % 2 == 0 else +1
            index = (j * j * 3 - j) // 2 # Calculate first pentagonal number
            if index > i: # If offset too large
                break
            item += partitions[i - index] * sign
            index += j
            if index > i:
                break
            item += partitions[i - index] * sign
            item %= MODULUS

        if item == 0:
            return str(i)
        partitions.append(item)

if __name__ == "__main__":
    print(compute())

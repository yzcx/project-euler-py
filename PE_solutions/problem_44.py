
# Project Euler problem 44: pentagon numbers

import itertools

def compute(): # Using a helper class to make code cleaner and efficient
    pentanum = PentagonalNumberHelper()
    min_d = None
    for i in itertools.count(2): # Infinite counter to generate pentagonal numbers until I found the answer
        pent_i = pentanum.term(i)
        if min_d is not None and pent_i - pentanum.term(i - 1) >= min_d: # Optimisation
            break
        for j in range(i - 1, 0, -1):
            pent_j = pentanum.term(j)
            diff = pent_i - pent_j
            if min_d is not None and diff >= min_d:
                break
            elif pentanum.is_term(pent_i + pent_j) and pentanum.is_term(diff): # Checking if sum and difference of two numbers are pentagonal
                min_d = diff
    return str(min_d)

class PentagonalNumberHelper:
    def __init__(self):
        self.term_list = [0]
        self.term_set = set()

    def term(self, x): # Gets the nth pentagonal number and generates new ones if needed
        assert x > 0
        while len(self.term_list) <= x:
            n = len(self.term_list)
            term = (n * (n * 3 - 1)) >> 1
            self.term_list.append(term)
            self.term_set.add(term)
        return self.term_list[x]

    def is_term(self, y):
        assert y > 0
        while self.term_list[-1] < y:
            n = len(self.term_list)
            term = (n * (n * 3 - 1)) >> 1
            self.term_list.append(term)
            self.term_set.add(term)
        return y in self.term_set

if __name__ == "__main__":
    print(compute())
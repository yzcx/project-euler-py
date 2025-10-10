
# Project Euler problem 93: arithmetic expressions

import itertools
import fractions

def longest_consecutive(abcd):
    expressible = set()
    ops_base = [0, 0, 0] + list(abcd)

    for ops in set(itertools.permutations(ops_base)): # Iterate over all unique arrangements of 4 digits and 3 operator slots
        for i in range(64):
            stack = []
            j = 0

            stackunderflow = False
            divbyzero = False

            for op in ops: # Evaluate RPN expression
                if 1 <= op <= 9:
                    stack.append(fractions.Fraction(op))
                elif op == 0:
                    if len(stack) < 2:
                        stackunderflow = True
                        break
                    right = stack.pop()
                    left = stack.pop()

                    oper = (i >> (j * 2)) & 3

                    if oper == 0:
                        stack.append(left + right)
                    elif oper == 1:
                        stack.append(left - right)
                    elif oper == 2:
                        stack.append(left * right)
                    elif oper == 3:
                        if right.numerator == 0:
                            divbyzero = True
                            break
                        stack.append(left / right)
                    j += 1
            if stackunderflow or divbyzero or len(stack) != 1:
                continue

            result = stack.pop()

            if result.denominator == 1 and result.numerator > 0:
                expressible.add(result.numerator)
    return next(i for i in itertools.count(1) if (i not in expressible)) - 1

def compute(): # Outer loop iterares over all 126 combos of four distinct digits
    ans = max(((a, b, c, d)
               for a in range(1, 10)
               for b in range(a + 1, 10)
               for c in range(b + 1, 10)
               for d in range(c + 1, 10)),
              key=longest_consecutive)
    return "".join(str(x) for x in ans)

if __name__ == "__main__":
    print(compute())
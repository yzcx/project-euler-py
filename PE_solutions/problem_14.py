
# Project Euler problem 14: longest collatz sequence

def count_collatz(number: int) -> int:
    count = 1
    n = number
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count

longest_chain = 0
longest_number = 0

if __name__ == "__main__":
    for n in range(1, 1000000): # Iterating through each number within range
        count = count_collatz(n) # Finding chain length for current num
        if count > longest_chain:
            longest_chain = count
            longest_number = n # Updating variables to store new longest chain and number that produced it

    print(longest_number)
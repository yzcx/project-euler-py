
# Project Euler problem 95: amicable chains

import itertools

def compute():
    LIMIT = 10 ** 6

    divisorsum = [0] * (LIMIT + 1) # Pre compute sum of proper divisors
    for i in range(1, LIMIT + 1):
        for j in range(i * 2, LIMIT + 1, i):
            divisorsum[j] += i

    maxchainlen = 0 # Find longest chain
    ans = -1
    for i in range(LIMIT + 1):
        visited = set()
        cur = i
        for count in itertools.count(1):
            visited.add(cur)
            next = divisorsum[cur]
            if next == i:
                if count > maxchainlen:
                    ans = i
                    maxchainlen = count
                break
            elif next > LIMIT or next in visited:
                break
            else:
                cur = next
    return str(ans)

if __name__ == "__main__":
    print(compute())
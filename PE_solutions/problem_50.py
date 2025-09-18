
# Project Euler problem 50: consecutive prime sum

def list_primality(n): # Sieve of Eratosthenes function again efficiently to generate boolean list of primes
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, n + 1, i):
                is_prime[multiple] = False
    return is_prime

def list_primes(n): # Helper function creating list of primes up to n
    is_prime = list_primality(n)
    primes = [i for i, is_p in enumerate(is_prime) if is_p]
    return primes

def compute():
    ans = 0
    limit = 999999
    isprime = list_primality(limit)
    primes = list_primes(limit)

    consecutive = 0
    for i in range(len(primes)):
        sum_of_primes = 0
        consec_count = 0
        for j in range(i, len(primes)):
            sum_of_primes += primes[j]
            consec_count += 1
            if sum_of_primes > limit:
                break
            if isprime[sum_of_primes] and consec_count > consecutive:
                ans = sum_of_primes
                consecutive = consec_count
    return str(ans)

if __name__ == "__main__":
    print(compute())
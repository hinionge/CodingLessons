# 23.8.2023

# Project Euler 10
# Summation of primes

# Find the sum of the primes below two million.

# 24.8.2023 -- this is more than ten times faster now that I've introduced a sieve into the prime check

import math
import time

def prime(n):
                                # Special cases:
    if n == 1 or n == 0:
        return False
    if n == 2:
        return True

    max = (int(math.ceil(math.sqrt(n))))

    sieve = [0]

    for s in range(max):
        sieve.append(1)

    d = 2
                                # Count up to sqrt(n)
    while d <= max:
                                # Only check a new divisor if it has not already been eliminated
        if sieve[d] == 1:
            if n % d == 0:
                return False
                                # If a number d does not divide n, then eliminate all multiples of d from the search
        for j in range(d,len(sieve),d):
            sieve[j] = 0
        d += 1

    return True


def sum_primes_below(max):
    n = 2
    primesum = 0
    count = 1
    while n < max:
        if prime(n):
                            # Output every 1000th prime, just to keep me happy it's still alive :)
            if count == 1000:
                print(n)
                count = 1

            count += 1
            primesum += n
        n += 1

    return primesum

if __name__ == "__main__":
    below = 2000000
    begin_clock = time.time()
    print ("The sum of primes below " + str(below) + " is " + str(sum_primes_below(below)))
    end_clock = time.time()-begin_clock

    print (end_clock, "seconds")
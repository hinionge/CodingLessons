# 23.8.2023

# Project Euler 10
# Summation of primes

# Find the sum of the primes below two million.



                            # Primality test
def prime(n):


                            # Special cases:
    if n == 1 or n == 0:
        return False
    if n == 2:
        return True

    d = 2

                            # Test each number up to n/2
    while d <= n // 2:
        if n % d == 0:
            return False
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
    print ("The sum of primes below " + str(below) + " is " + str(sum_primes_below(below)))
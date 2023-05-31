import math


def x_divides_y(x, y):
    factor = True
    if x % y != 0:
        factor = False
    return factor


def prime(n):
    ans = True
    half = int(n / 2)
                            # (test counts down from half of in, one integer at a time, asks if it divides:
    for c in range(half, 1, -1):
        # (if it ever does, n is not prime)
        if x_divides_y(n, c) == True:
            ans = False
                            # There is a special case for excluding 1, which would otherwise return as prime
    if n == 1:
        ans = False
    return ans


def factors(n, incl_n):
    factors = []

    for j in range(1, math.ceil(n / 2) + 1):
        if n % j == 0:
            factors.append(j)

    if incl_n:
        factors.append(n)

    return factors

def prime_factors(n):
    prime_factors = []
    factors_of_n = []
    factors_of_n = factors(n, True)

    for e in range(len(factors_of_n)):
        if prime(factors_of_n[e]) == True:
            prime_factors.append(factors_of_n[e])

    return prime_factors

if __name__ == "__main__":
    print(prime_factors(46189))
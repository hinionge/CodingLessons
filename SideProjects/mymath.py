
import math

class mymath:

    def second_divides_first(x,y):
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
            if mymath.second_divides_first(n, c) == True:
                ans = False
                            # There is a special case for excluding 1, which would otherwise return as prime
        if n == 1:
            ans = False
        return ans

    def factors(n,incl_n):

        factors = []

        for j in range(1,math.ceil(n/2)+1):
            if n%j == 0:
                factors.append(j)

        if incl_n:
            factors.append(n)

        return factors


    def prime_factors(n,incl_one):

        prime_factors = []
        factors = mymath.factors(n,True)

        if incl_one:
            prime_factors.append(1)

        for e in range(len(factors)):
            if mymath.prime(factors[e]) == True:
                prime_factors.append(factors[e])

        return prime_factors



if __name__ == "__main__":


    print(mymath.factors(8040,True))
    print(mymath.prime_factors(8040,False))
    for k in range (1,7):
        print(str(k) + ": " + str(mymath.prime(k)))
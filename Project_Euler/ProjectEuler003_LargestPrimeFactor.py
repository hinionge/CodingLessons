
# 8.3.2023 Revisiting some Project Eulers I lost in December

# this doesn't work yet

import time

                            # Method returns True if m divides n with modulo zero
def does_it_divide(m,n):
    factor = True
    if n%m != 0:
        factor = False
    return factor

                            # Primality test
def is_it_prime(n):
    prime = True
    half = int(n/2)
                            # (test counts down from half of n, one integer at a time, asks if it divides:
    for c in range(half,1,-1):
                            # (if it ever does, n is not prime)
        if does_it_divide(c,n) == True:
            prime = False
                            # There is a special case for excluding 1, which would otherwise return as prime
    if n == 1:
        prime = False
    return prime

def find_largest_prime_factor(n):
    ans = 1
    found = False
    div = 2
    while found == False:
        if does_it_divide(div,n):
            if is_it_prime(n/div):
                ans = n/div
                found = True
        div = div + 1
    return int(ans)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    inputn = input("Test number: ")
    inputn = int(inputn)

    timestart = time.time()
    f = find_largest_prime_factor(inputn)
    print(f)
    timer = time.time()-timestart

    print (timer, "seconds")
import math




def fibonacci(a,b):
    c = a + b
    return c


def prime(n):
    check = True
    for j in range(2,n):
        if n % j == 0:
            check = False
    if n == 0:
        check = False
    return check


def primebelow(n):
    p = n

    while not prime(p):
        p -= 1

    return p

def primeabove(n):
    p = n

    while not prime(p):
        p += 1

    return p

def ppt(a,b):
    c = 0
    pb = primebelow(a*b)
    pa = primeabove(a*b)

    c = (pa-pb)+a     #  GOOD

    print(c)

    return int(c)

def sequence(length):
    seq = [2,2]
    for j in range(length):
        seq.append(ppt(seq[j],seq[j+1]))
    return seq


if __name__ == "__main__":
    print(sequence(777))
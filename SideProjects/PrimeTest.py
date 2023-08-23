# 23.8.2023

# Another test for primes, wasn't happy with the previous

def prime(n):
                                # Special cases:
    if n == 1 or n == 0:
        return False
    if n == 2:
        return True

    d = 2

                                # Test each number up to n/2
    while d <= n//2:
        if n % d == 0:
            return False
        d += 1

    return True





if __name__ == "__main__":
    for n in range (50):

        star = ""

        if prime(n):
            star = " *"
        print(str(n) + star)
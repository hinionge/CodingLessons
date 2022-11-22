
import time

# Start a list of primes, to add to, so that once we've calculated something's prime
# once, we don't need to do so again
listofprimes = []

def does_m_divide_n(m,n):
# Simple mod test for divisibility
    if (n%m == 0):
        return True
    else:
        return False

    # def is_n_prime(n):
    # # i.e., only calculate whether it's prime if it's not on the list
    #     if listofprimes.count(n) == 0:
    #         # start counting factors
    #         factors = 0
    #         c = 2
    #         while c <= n/2:
    #             # counting up, dividing by prime numbers only...
    #             if is_n_prime(c) == True:
    #                 # if we find a divisor, count it as a factor by adding to the tally
    #                 if does_m_divide_n(c,n) == True:
    #                     factors = factors + 1
    #             c = c+1
    #
    # # if it has more than zero factors (by this tally, anyway) it isn't prime
    #         if factors > 0:
    #             return False
    # # if it has no factors then it's prime, so, add it to the list, and return YES this is prime
    #         else:
    #             listofprimes.append(n)
    #         #    print (listofprimes[-1])
    #             return True
    #     else:
    #     #    print ("ignoring",n , "cause it's on the list") #this was just a test bit during coding
    #         return True

def is_n_prime(n):
    top = n
    bottom = 1
    f = 1
    integercount = 0
    while f >= 1:
#        print(integercount)
        if f%1 == 0:
            integercount = integercount + bottom
        f = top/bottom
        top = top-bottom
        bottom = bottom + 1

    if integercount == 6:
    #    print (n, "is prime")
        return True
    if  n == 2:
        return True
    else:
    #    print (n, "is not prime")
        return False

# the actual Project Euler problem:
def find_largest_prime_factor(n):
#   May as well check if it's prime first
    if is_n_prime(n) == True:
        print (n, "is prime, so", n, "is its largest and only divisor")
#   Start at 2, divide by increasingly larger numbers
#   So that the first prime divisor found... must be the largest? Does that work?
#   It does seem to work but it gets very slow very quickly when nos get big
    for x in range (2,n):
        if does_m_divide_n(x,n) == True:
#      I ran into some trouble with floats and integers here and couldn't quite figure why but this next line fixed it
            divisor = int(n/x)
            if is_n_prime(divisor) == True:
                print ("Largest prime factor of", n, "is", divisor)
                break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    inputn = input("Test number:")
    inputn = int(inputn)

    timestart = time.time()
    find_largest_prime_factor(inputn)
    timer = time.time()-timestart

    print (timer, "seconds")

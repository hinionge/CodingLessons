import math

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
# ... with an if statement:
    if  n == 2:
        return True
    else:
    #    print (n, "is not prime")
        return False

def ConvSecstoMS(t):
    s = ""
    s = s+str(math.trunc(t/60))+"m "+str(t % 60)+"s"
    #print s
    return s

def printtimes(n,m):
    c = 0
    for t in range (n,m):
        if is_n_prime(t) == True:
        #    print (t)
            print (ConvSecstoMS(t))
            c = c+1
    print (c)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    printtimes(680,1023)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

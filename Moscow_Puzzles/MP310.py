


def divides(m,n):
    ans = True
    if m%n != 0:
        ans = False

    return ans


def oranges(n):
    tickboxes = ""
    for k in range (10,1,-1):
        if divides(n+1,k):
            tickboxes = tickboxes + "#"
        else:
            tickboxes = tickboxes + " "
    if tickboxes == "#########":
        tickboxes = tickboxes + "   <<<<<<<<<<<<< " + str(n)
    print(tickboxes)



if __name__ == "__main__":
    for j in range(2525):
        oranges(j)
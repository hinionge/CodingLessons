def fizz_buzz (number):
    outstring = ""
    for y in range(number):
        outstring = ""
        if (y % 3 == 0):
            outstring = outstring+"Fizz"

        if (y % 5 == 0):
            outstring = outstring+"Buzz"

        print(y, ": ", outstring)

if __name__ == '__main__':
	fizz_buzz(15)

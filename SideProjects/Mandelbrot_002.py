
# 26.2.2023
#
# The Mandelbrot Set
#
# I can't believe I actually made it work....... honestly, I've been wanting to code this since I was about twelve

import math
import cmath

def add_point(s,filled):
    if filled == 0:
        s = s + " "
    if filled == 1:
        s = s + "•"
    return s

def checkpoint(c):
    z = complex(0,0)
    filled = 0
    itercount = 0

    for iter in range (200):
        if z.real**2 + z.imag**2 > 2:
            z = complex(2,0)


        # Mandelbrot set
        z = z**2 + c

        # Burning Ship fractal
        # z = (abs(z.real) + abs(z.imag)*complex(0,1))**2 + c





    if z.real**2 + z.imag**2 > 2:
        filled = 1

    return filled

def plot_mandelbrot(xmin,xmax,ymin,ymax):
    output = ""
    for y in range(ymin,ymax,-2):
        y = y / (ymax-ymin)*2
        for x in range(xmin,xmax):
            x=x/50
            output = add_point(output,checkpoint(complex(x,y)))
        output = output + "\n"
    print(output)

if __name__ == '__main__':
    xmin = -100
    xmax = 50
    ymin = 40
    ymax = -40

    userinput = ""
    increment = 20

    while userinput != "quit":
        print("\n,")
        plot_mandelbrot(xmin, xmax, ymin, ymax)
        userinput = input()
        if userinput == ",":
            xmin = xmin - increment
            xmax = xmax - increment
        if userinput == ".":
            xmin = xmin + increment
            xmax = xmax + increment
        if userinput == "a":
            ymin = ymin + increment
            ymax = ymax + increment
        if userinput == "z":
            ymin = ymin - increment
            ymax = ymax - increment

        if userinput == "[":
            ymin = ymin - increment
            ymax = ymax + increment
            xmin = xmin - increment
            xmax = xmax + increment

        if userinput == "]":
            ymin = ymin + increment
            ymax = ymax - increment
            xmin = xmin + increment
            xmax = xmax - increment
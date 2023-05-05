# 5.5.2023
# Basic implicit heap, plus a bodge of a visualization of heap in tree shape. I'm determined to get this!
# edit: and it DOES work -- at last
# Next is to 1) make a heapsort from this; and 2) do all this with nodes and classes, I guess

import random

def max_heapify(a, size, i):
    leftchild = 2 * i
    rightchild = 2 * i + 1

    max = i

    if leftchild < size and a[leftchild] > a[i]:
        max = leftchild

    if rightchild < size and a[rightchild] > a[max]:
        max = rightchild

    if max != i:
        a[i], a[max] = a[max], a[i]
        max_heapify(a, size, max)

def build_max_heap(a):
    size = len(a)

    for i in range (size//2, 0, -1):
        max_heapify(a, size, i)

def display_heap(heap):
    # This isn't pretty but it KIND OF outputs the heap to give a visual sense of it

    width = 60
    index = 1
    layer = 0
    count = 0

    output = ""

    while index <= len(heap)-1:

        for pad in range(int(width / 2 ** (layer)+1)):
            output = output + " "

        output = output + str(heap[index])
        cutoff = 2 ** layer - 1
        index += 1
        count += 1

        if count > cutoff:
            output = output + "\n\n"
            layer = layer + 1
            count = 0

    return output


if __name__ == "__main__":
    a = [None]
    for j in range(31):
        a.append(random.randint(1,200))

    print(a)
    print(display_heap(a))
    print("\n\n")

    build_max_heap(a)

    print(a)
    print(display_heap(a))


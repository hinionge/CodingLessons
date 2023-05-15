# 15.5.2023
# Insertion Sort


import math
import random
import time


def InsertionSort(a):
    length = len(a)

    sorted = []

    for item in range(length):
        sorted.append(a[item])
        for j in range(item,0,-1):
            if sorted[j] < sorted[j-1]:
                sorted[j], sorted[j-1] = sorted[j-1], sorted[j]

    return sorted



if __name__ == "__main__":
    a = []
    for j in range(73):
        a.append(random.randint(1, 200))


    print(a)

    start = time.time()
    a = InsertionSort(a)
    elapsed = time.time()-start
    print("Sorted by insertion sort in " + str(elapsed) + " seconds:")
    print(a)
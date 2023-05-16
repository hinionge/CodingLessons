# 15.5.2023
# Binary Insertion Sort




import math
import random
import time


def binary_search(a, val, start, end):

    if start == end:
        if a[start] > val:
            return start
        else:
            return start + 1

    if start > end:
        return start

    mid = (start + end) // 2
    if a[mid] < val:
        return binary_search(a, val, mid + 1, end)
    elif a[mid] > val:
        return binary_search(a, val, start, mid - 1)
    else:
        return mid


def BinaryInsertionSort(a):
    for i in range(1, len(a)):
        val = a[i]
        j = binary_search(a, val, 0, i-1)
        a = a[:j] + [val] + a[j:i] + a[i + 1:]
    return a



if __name__ == "__main__":
    a = []
    for j in range(73):
        a.append(random.randint(1, 200))


    print(a)

    start = time.time()
    a = BinaryInsertionSort(a)
    elapsed = time.time()-start
    print("Sorted by bianry insertion sort in " + str(elapsed) + " seconds:")
    print(a)
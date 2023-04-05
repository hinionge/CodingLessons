# 2.4.2023
# Prep stages for coding some sorting algorithms, simply so I don't have to do it in the morning

import random


def binary_search(list, value, start, end):

    if start == end:
        if list[start] > value:
            return start
        else:
            return start + 1

    if start > end:
        return start

    mid = (start + end) // 2

    if list[mid] < value:
        return binary_search(list, value, mid+1, end)
    elif list[mid] > value:
        return binary_search(list, value, start, mid-1)
    else:
        return mid


def insertion_sort(list):
    for j in range(1,len(list)):
        key = list[j]
        i = j - 1
                            # Changed from > 0 in CLRS to > -1 to handle zero-indexing
        while i > -1 and list[i] > key:
            list[i+1] = list[i]
            i = i - 1
        list[i+1] = key

    return list

def binary_insertion_sort(list):
    for i in range(1,len(list)):
        key = list[i]
        j = binary_search(list, key, 0, i-1)
                            # This line here I don't follow
        list = list[:j] + [key] + list[j:i] + list[i+1:]
    return list




                            # 5.4.2023 third or fourth attempt at Quick Sort
                            # .... first step SEEMS to work? though it doesn't always catch every number, for some reason
                            #
                            # While trying to code it, using inbuilt pop() and insert() rather than 'manually' handling list items, for simplicity


def quick_sort(list):
                            # Traps for when recursion has gone far enough and the list is 1 or 2 elements
    if len(list) == 0:
        return list
    if len(list) == 1:
        return list
    elif len(list) == 2:
        if list[0] > list[1]:
            temp = list[0]
            list[0] = list[1]
            list[1] = temp
            return list
    else:
        #peg = random.randint(1,len(list)-2)
                            # Stick with peg at index 5 while trying to make it work
        peg = 5
        print("Peg at index " + str(peg) + ": L/R sort value is " + str(list[peg]))

        height = list[peg]


                            # Loop to find numbers to the left of peg which are larger: if found, adds to end of list and removes in position
        j = 0
        while peg > 1 and j < peg+1:
            if list[j] > height:
                list.append(list[j])
                list.pop(j)
                peg -= 1
                j -= 1
            j += 1

                            # Loop to find numbers on right of peg which are smaller, and shove them to the start of the list
        for j in range(peg,len(list)-1):
            if list[j] < height:
                list.insert(0,list[j])
                list.pop(j+1)

        return list

                            # Placeholder for merge sort
def merge_sort(list):
    pass


                            # Simple generation of random list of integers
def generate_random_list(length,intmin,intmax):
    randomlist = []

    for j in range(length):
        k = random.randint(intmin,intmax)
        randomlist.append(k)

    return randomlist


if __name__ == "__main__":
    length = 15
    upper = 1
    lower = 100
    #                         # Generate a list of 100 random numbers between 1 and 100 inclusive
    # mylist = generate_random_list(length,upper,lower)
    # print("\nUnsorted list:")
    # print(mylist)
    #
    #                         # Demonstrate insertion sort
    # mylist = insertion_sort(mylist)
    # print("Insertion sort:")
    # print(mylist)
    #
    #                         # Another random list
    # mylist = generate_random_list(length,upper,lower)
    # print("\nUnsorted list:")
    # print(mylist)
    #
    # mylist = binary_insertion_sort(mylist)
    # print("Binary insertion sort:")
    # print(mylist)

                            # Another random list
    mylist = generate_random_list(length,upper,lower)
    print("\nUnsorted list:")
    print(mylist)

    mylist = quick_sort(mylist)
    print(mylist)
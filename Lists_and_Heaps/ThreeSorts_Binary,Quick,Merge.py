# 2.4.2023
# Prep stages for coding some sorting algorithms, simply so I don't have to do it in the morning

import random

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

                            # Placeholder for binary sort
def binary_sort(list):
    pass

                            # Placeholder for quick sort
def quick_sort(list):
    pass

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
    length = 43
    upper = 1
    lower = 100
                            # Generate a list of 100 random numbers between 1 and 100 inclusive
    mylist = generate_random_list(length,upper,lower)
    print("\nUnsorted list:")
    print(mylist)

                            # Demonstrate insertion sort
    mylist = insertion_sort(mylist)
    print("Insertion sort:")
    print(mylist)

                            # Another random list
    mylist = generate_random_list(length,upper,lower)
    print("\nUnsorted list:")
    print(mylist)
# 2.4.2023
# Prep stages for coding some sorting algorithms, simply so I don't have to do it in the morning

import random as rnd

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
        k = rnd.randint(intmin,intmax)
        randomlist.append(k)

    return randomlist


if __name__ == "__main__":
                            # Generate a list of 100 random numbers between 1 and 100 inclusive
    mylist = generate_random_list(100,1,100)
    print("Unsorted list:")
    print(mylist)
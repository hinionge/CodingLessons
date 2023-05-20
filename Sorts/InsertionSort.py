# 15.5.2023
# Insertion Sort

# 16.5.2023
# Insertion Sort but rewritten -- previous was really just bubble sort in reverse (swapping still happened indivudually)
# Re-coding now to preserve this distinction:
# -- bubble sort the new item moves one swap by swap til it arrives in place
# -- insertion sort, the correct place is found first and the new item placed there subsequently

# 20.5.2023
# Just a little note to self that this, somehow, took about five hundred attempts.
# I repeatedly failed to notice that once a position to insert the new value had been found,
#   it kept being added to, every time a larger value was found, up to the item to be inserted

# Very relieved to have finally cracked this one. It was so simple, and I hated it (lol)



import math
import random
import time



def InsertionSort(arr):

    for i in range (1,len(arr)):

        j = 0

        while arr[j] < arr[i]:
            j += 1
        pos = j

        arr.insert(pos, arr[i])

        del arr[i+1]


    return arr




if __name__ == "__main__":
    arr = []
    for j in range(23):
        arr.append(random.randint(1, 200))

    print(arr)


    start = time.time()
    arr = InsertionSort(arr)
    elapsed = time.time()-start
    print("Sorted by insertion sort in " + str(elapsed) + " seconds:")
    print(arr)
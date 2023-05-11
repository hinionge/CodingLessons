# Merge sort

# Committing to Git at this point because it's late already and I'm too tired for this (!)
# It seemed to work, before, but only on lists of identical length

# But I'll upload with this exact input because the output shows:
# [1, 3, 2, 4, 5, 7, 6, 8]

# So it isn't working right at the start...


def merge(left,right):
    merged = []

    size = len(left) + len(right)

    while len(merged) < size:
        small_left = left[0]
        small_right = right[0]

        for j in range(len(left)):
            if left[j] < small_left:
                small_left = left[j]

        for j in range(len(right)):
            if right[j] < small_right:
                small_right = right[j]

        left.remove(small_left)
        right.remove(small_right)

        if small_left < small_right:
            merged.append(small_left)
            merged.append(small_right)
        else:
            merged.append(small_right)
            merged.append(small_left)



    return merged


if __name__ == "__main__":

    a = [4,7,3,8]
    b = [1,2,6,5]

    print(merge(a,b))
# Possibly written during a session

def quickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        print(pivot, "pivot")
        for i in arr:
            if i < pivot:
                less.append(i)
                print(less, "less")
            elif i > pivot:
                more.append(i)
                print(more, "more")
            else:
                pivotList.append(i)
                print(pivotList, "pivlist")
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more


if __name__ == "__main__":

    a = [6,9,7,2,1]

    print(a)

    a = quickSort(a)

    print(a)
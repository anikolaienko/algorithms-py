def quickSort(array):
    quickSortPart(array, 0, len(array) - 1)


def quickSortPart(array, lo, hi):
    if hi <= lo:
        return
    j = partition(array, lo, hi)
    quickSortPart(array, lo, j - 1)
    quickSortPart(array, j + 1, hi)


def partition(array, lo, hi):
    i, j = lo + 1, hi
    while True:
        while i < hi and array[i] < array[lo]:
            i += 1
        while j > lo and array[j] >= array[lo]:
            j -= 1
        if i >= j:
            break

        array[i], array[j] = array[j], array[i]

    array[lo], array[j] = array[j], array[lo]
    return j

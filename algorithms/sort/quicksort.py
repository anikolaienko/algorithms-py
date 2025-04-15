def quick_sort(array: list[int], algo: str = "hoare"):
    if algo.lower() == "lumoto":
        _quick_sort_lumoto(array, 0, len(array) - 1)
    elif algo.lower() == "hoare":
        _quick_sort_hoare(array, 0, len(array) - 1)


def _quick_sort_lumoto(array, lo, hi):
    if lo >= hi or lo < 0:
        return
    
    j = _partition_lumoto(array, lo, hi)

    _quick_sort_lumoto(array, lo, j - 1)
    _quick_sort_lumoto(array, j + 1, hi)


def _partition_lumoto(array, lo, hi):
    # Choose the last element as the pivot
    pivot = array[hi]

    # Temporary pivot index
    i = lo

    for j in range(lo, hi):
        # If the current element is less than or equal to the pivot
        if array[j] <= pivot:
            # Swap the current element with the element at the temporary pivot index
            array[i], array[j] = array[j], array[i]
            # Move the temporary pivot index forward
            i += 1

    # Swap the pivot with the last element
    array[i], array[hi] = array[hi], array[i]
    return i


def _quick_sort_hoare(array, lo, hi):
    if lo >= hi or lo < 0:
        return
    
    p = _partition_hoare(array, lo, hi)

    _quick_sort_hoare(array, lo, p - 1)
    _quick_sort_hoare(array, p + 1, hi)


def _partition_hoare(array, lo, hi):
    # Pivot value
    pivot = array[lo]

    # Left and right indexes
    i, j = lo, hi
    while True:
        # Move the left index to the right while the element at 
        # the left index is less than the pivot
        while array[i] < pivot:
            i += 1

        # Move the right index to the left while the element at
        # the right index is greater than the pivot
        while array[j] > pivot:
            j -= 1

        # If the indices crossed, return
        if i >= j:
            break

        # Swap the elements at the left and right indices
        array[i], array[j] = array[j], array[i]
        i += 1

    return j

def merge_sort(arr: list[int], inplace: bool = False) -> list[int]:
    if not inplace:
        arr = arr.copy()
    
    return _merge_sort(arr)


def _merge_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = _merge_sort(arr[:mid])
    right = _merge_sort(arr[mid:])

    i, j, k = 0, 0, 0
    while i < len(left) or j < len(right):
        if j >= len(right) or (i < len(left) and left[i] <= right[j]):
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    return arr
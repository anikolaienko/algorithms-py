def quickselect(array, k):
    l, r = 0, len(array) - 1
    k -= 1

    while l < r:
        i, j = l + 1, r
        while i <= j:
            while i <= j and array[l] > array[i]:
                i += 1
            while j >= i and array[l] < array[j]:
                j -= 1

            if i < j:
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1

        if array[j] < array[l]:
            array[l], array[j] = array[j], array[l]

        if j == k:
            return array[j]
        if j > k:
            r = j - 1
        else:
            l = j + 1

    return array[l]

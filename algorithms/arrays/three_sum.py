def bin_search(array, left, right, target):
    while left < right:
        mid = (left + right) // 2
        if array[mid] > target:
            right = mid
        elif array[mid] < target:
            left = mid + 1
        else:
            return array[mid]
    return None

def threeNumberSum(array, targetSum):
    array = sorted(array)

    result = []
    for i, a in enumerate(array[:-2]):
        for j, b in enumerate(array[i+1:-1]):
            c = bin_search(array, i + j + 2, len(array), targetSum - a - b)
            if c is not None:
                result.append([a, b, c])

    return result


if __name__ == "__main__":
    expected = [
        [-8, 2, 6],
        [-8, 3, 5],
        [-6, 1, 5]
    ]
    assert expected == threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0)

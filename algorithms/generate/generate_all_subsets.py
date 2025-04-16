def generate_all_subsets(arr: list[int], algo: str) -> list[list[int]]:
    if algo == "recursive":
        return _generate_subset_recursive([], arr, 0)
    if algo == "bin":
        return _generate_subset_bin(arr)
    raise NotImplementedError()


def _generate_subset_recursive(curr: list[int], sample: list[int], position: int) -> list[list[int]]:
    if position >= len(sample):
        return [curr]
    
    subset_a = _generate_subset_recursive(curr, sample, position + 1)
    subset_b = _generate_subset_recursive(curr + [sample[position]], sample, position + 1)
    
    return subset_a + subset_b


def _generate_subset_bin(arr: list[int]) -> list[list[int]]:
    n = len(arr)

    result = []
    for k in range(0, 1 << n):
        sample = []
        for i in range(n):
            if k & (1 << i):
                sample.append(arr[i])
        result.append(sample)

    return result


if __name__ == "__main__":
    arr = [1,2,3,4]

    # print("All combinations (recursive):\n" + "\n".join(map(str, generate_all_subsets(arr, "recursive"))))
    print("All combinations (bin):\n" + "\n".join(map(str, generate_all_subsets(arr, "bin"))))

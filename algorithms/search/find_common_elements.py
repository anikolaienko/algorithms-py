import time

def find_common_elements(arr1: list[int], arr2: list[int], algo="sort") -> list[int]:
    start = time.time_ns()
    try:
        if algo == "sort":
            return _find_common_by_sorting(arr1, arr2)
        elif algo == "set":
            return _find_common_by_set(arr1, arr2)
        else:
            raise NotImplementedError()
    finally:
        end = time.time_ns()
        print(f"Total time: {start - end} ns")


def _find_common_by_sorting(arr1: list[int], arr2: list[int]) -> list[int]:
    left_arr_iter = iter(sorted(arr1))
    right_arr = list(sorted(arr2))
    
    result = []
    left_x = next(left_arr_iter, None)
    for x in right_arr:
        while left_x is not None and left_x < x:
            left_x = next(left_arr_iter, None)
        
        if left_x == x:
            result.append(x)
    
    return result
            

def _find_common_by_set(arr1: list[int], arr2: list[int]) -> list[int]:
    left_set = set(arr1)
    return [x for x in arr2 if x in left_set]


if __name__ == "__main__":
    import random
    random.seed()
    
    population = list(range(1000000))

    a = random.sample(population, 10000)
    b = random.sample(population, 10000)

    print("Common (sort) ", find_common_elements(a, b, "sort"))
    print("Common (set) ", find_common_elements(a, b, "set"))

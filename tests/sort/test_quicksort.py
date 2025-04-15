import pytest

from algorithms.sort.quicksort import quick_sort

@pytest.mark.parametrize("arr", 
                        [
                            [],
                            [1],
                            [2,1],
                            [9,1,5,2,5,9,2],
                            [1,2,3,4,5,6,7,8,9],
                            [9,8,7,6,5,4,3,2,1],
                            [9,9,9,9,9,9,9,9,9],
                            [6,5,6,5,6,5,6,5,6],
                            [6,6,6,6,6,5,5,5,5,5]
                        ]
)
def test_quick_sort(arr: list[int]):
    expected = list(sorted(arr))
    hoare_result = arr.copy()
    lumoto_result = arr.copy()
    
    quick_sort(hoare_result, algo="hoare") 
    quick_sort(lumoto_result, algo="lumoto")

    assert hoare_result == expected
    assert lumoto_result == expected

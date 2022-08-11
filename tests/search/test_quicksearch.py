from algorithms.search.quickselect import quickselect
import pytest

testdata = [
    ([8, 5, 2, 9, 7, 6, 3], 3, 5),
    ([1], 1, 1),
    ([43, 24, 37], 1, 24),
    ([1, 3, 71, 123, 124, 156, 814, 1294, 10024, 110000, 985181, 55516151], 4, 123)
]

@pytest.mark.parametrize("arr, k, expected", testdata)
def test_quickselect(arr, k, expected):
    assert quickselect(arr, k) == expected

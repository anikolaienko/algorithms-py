from algorithms.sum_min_sums import findTotalPowerSlow
import pytest

testdata = [
    ([1, 2, 3], 33),
    ([2, 3, 2, 1], 69),
    ([8, 5, 2, 9, 7, 6, 3], 1473),
    ([1], 1),
    ([43, 24, 37], 9362),
    ([1, 3, 71, 123, 124, 156, 814, 1294, 10024, 110000, 985181, 55516151], 32623303)
]

@pytest.mark.parametrize("arr, expected", testdata)
def test_findTotalPower(arr, expected):
    assert findTotalPowerSlow(arr) == expected

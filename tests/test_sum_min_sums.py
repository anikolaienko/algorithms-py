from algorithms.sum_min_sums import findTotalPower, findTotalPowerSlow
import pytest

testdata = [
    ([1, 2, 3]),
    ([2, 3, 2, 1]),
    ([8, 5, 2, 9, 7, 6, 3]),
    ([1]),
    ([43, 24, 37]),
    ([1, 3, 71, 123, 124, 156, 814, 1294, 10024, 110000, 985181, 55516151])
]

@pytest.mark.parametrize("arr", testdata)
def test_findTotalPower(arr):
    expected = findTotalPowerSlow(arr)
    assert findTotalPower(arr) == expected

import pytest
from algorithms.count_rectangles import count_rectangles


testdata = [
    ([[0, 0],[0, 1],[1, 1],[1, 0],[2, 1],[2, 0],[3, 1],[3, 0]], 6)
]


@pytest.mark.parametrize("coords, expected_count", testdata)
def test_count_rectangles(coords, expected_count):
    assert count_rectangles(coords) == expected_count

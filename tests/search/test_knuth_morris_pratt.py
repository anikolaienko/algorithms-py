import pytest
from algorithms.search.knuth_morith_pratt import knuthMorrisPratt


testdata = [
    ("aefoaefcdaefcdaed", "aefcdaed", True),
    ("aefoaefcdaefcdaet", "aefcdaed", False),
    ("aabc", "abc", True),
]

@pytest.mark.parametrize("string, substring, expected", testdata)
def test_knuth_moriss_pratt(string, substring, expected):
    assert knuthMorrisPratt(string, substring) == expected

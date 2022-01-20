from algorithms.arrays.no_duplicates import no_duplicates

def test_no_duplicates__no_repeating():
    assert no_duplicates('abcd')

def test_no_duplicates__repeating_a():
    assert no_duplicates('abcda') == False

def test_no_duplicates__one_char():
    assert no_duplicates('a')

def test_no_duplicates__empty_str():
    assert no_duplicates('')

def test_no_duplicates__5_a():
    assert no_duplicates('aaaaa') == False

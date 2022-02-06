from algorithms.arrays import all_unique_characters

def test_all_unique_characters__no_repeating():
    assert all_unique_characters('abcd')

def test_all_unique_characters__repeating_a():
    assert all_unique_characters('abcda') == False

def test_all_unique_characters__one_char():
    assert all_unique_characters('a')

def test_all_unique_characters__empty_str():
    assert all_unique_characters('')

def test_all_unique_characters__5_a():
    assert all_unique_characters('aaaaa') == False

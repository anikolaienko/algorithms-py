from algorithms.arrays import calc_min_max_window_diff

def test_calc_min_max_window_diff__1():
    assert calc_min_max_window_diff([1]) == 0

def test_calc_min_max_window_diff__1_1():
    assert calc_min_max_window_diff([1, 1]) == 0

def test_calc_min_max_window_diff__1_1_1():
    assert calc_min_max_window_diff([1, 1, 1]) == 0

def test_calc_min_max_window_diff__1_2_3():
    assert calc_min_max_window_diff([1, 2, 3]) == 4

def test_calc_min_max_window_diff__2_1_3():
    assert calc_min_max_window_diff([2, 1, 3]) == 5

def test_calc_min_max_window_diff__4_2_1_3():
    assert calc_min_max_window_diff([4, 2, 1, 3]) == 2 + (3 + 1) + (3 + 2 + 2)

def test_calc_min_max_window_diff__4_2_4_4():
    assert calc_min_max_window_diff([4, 2, 4, 4]) == 2 + (2 + 2) + (2 + 2 + 0)

def test_calc_min_max_window_diff__1_2_4_3_5_2():
    assert calc_min_max_window_diff([1, 2, 4, 3, 5, 2]) == 1 + (3 + 2) + (3 + 2 + 1) + (4 + 3 + 2 + 2) + (4 + 3 + 3 + 3 + 3)

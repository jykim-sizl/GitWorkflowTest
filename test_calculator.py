from calculator import calculate_sum


def test_basic_sum():
    assert calculate_sum([1, 2, 3]) == 6


def test_empty_list():
    assert calculate_sum([]) == 0


def test_negative_numbers():
    assert calculate_sum([-1, -2, -3]) == -6


def test_floats():
    assert calculate_sum([1.5, 2.5]) == 4.0


def test_single_element():
    assert calculate_sum([42]) == 42

from bug_code import calculate_average, is_positive

def test_average_normal():
    assert calculate_average([1, 2, 3]) == 2.0

def test_positive_true():
    assert is_positive(5) is True

def test_positive_false():
    assert is_positive(-3) is False

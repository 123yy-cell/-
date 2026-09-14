from merge_sort import merge_sort

def test_given_input():
    # 题目给定的测试输入
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    assert merge_sort(arr) == [1, 1, 2, 3, 4, 5, 6, 9]

def test_duplicate_elements():
    # 含大量重复元素的测试用例
    arr = [2, 2, 1, 3, 2, 5, 4, 2]
    assert merge_sort(arr) == [1, 2, 2, 2, 2, 3, 4, 5]

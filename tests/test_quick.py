from sorting.quick.quick import quick_sort

array1 = [8, 4, 23, 42, 16, 15]
quick_sort(array1, 0, len(array1) - 1)

def test_quick_sort1():
    actual = array1
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected

array2 = [7, 8, 4, 3, 2, 9]
quick_sort(array2, 0, len(array2) - 1)

def test_quick_sort2():
    actual = array2
    expected = [2, 3, 4, 7, 8, 9]
    assert actual == expected

array3 = [-1, 8, 2, -3]
quick_sort(array3, 0, len(array3) - 1)

def test_quick_sort3():
    actual = array3
    expected = [-3, -1, 2, 8]
    assert actual == expected


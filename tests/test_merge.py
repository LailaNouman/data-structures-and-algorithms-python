import pytest
from sorting.merge.merge import merge_sort

arr = [8, 4, 23, 42, 16, 15]
merge_sort(arr)

def test_merge_sort1():
    actual = arr
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected

arr1 = [7,8,4,3,2]
merge_sort(arr1)

def test_merge_sort2():
    actual = arr1
    expected = [2, 3, 4, 7, 8]
    assert actual == expected

arr2 = [-1,8,2,-3]
merge_sort(arr2)

def test_merge_sort3():
    actual = arr2
    expected = [-3,-1,2,8]
    assert actual == expected
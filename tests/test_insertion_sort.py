import pytest
from sorting.insertion.insertion import insertion_sort

arr = [5, 4, 8, 2, 1]
insertion_sort(arr)

def test_insertion_sort1():
    actual = arr
    expected = [1,2,4,5,8]
    assert actual == expected

arr1 = [7,8,7,5,7,5]
insertion_sort(arr1)

def test_insertion_sort2():
    actual = arr1
    expected = [5,5,7,7,7,8]
    assert actual == expected

arr2 = [-1,8,2,-3]
insertion_sort(arr2)

def test_insertion_sort3():
    actual = arr2
    expected = [-3,-1,2,8]
    assert actual == expected
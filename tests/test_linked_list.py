import pytest
from linked_list.linkedlist import (
LinkedList
)

ll = LinkedList()

def test_empty_list():
    actual = ll.toString()
    expected = 'Empty list'
    assert actual == expected

def test_insert():
    ll.insert(3)
    actual = ll.toString()
    expected = [3]
    assert actual == expected

def test_kth_where_list_size_is_one():
    actual = ll.kth_from_end(0)
    expected = 3
    assert actual == expected

def test_insert_multi():
    ll.insert(5)
    ll.insert(6)
    actual = ll.toString()
    expected = [6, 5, 3]
    assert actual == expected

def test_kth_where_k_and_length_same():
    actual = ll.kth_from_end(2)
    expected = 6
    assert actual == expected

def test_includes():
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    actual = ll.includes(5)
    expected = True
    assert actual == expected

def test_kth_middle():
    actual = ll.kth_from_end(4)
    expected = 4
    assert actual == expected

def test_insert_before():
    ll.insert_before(1,2)
    actual = ll.toString()
    expected = [2, 5, 4, 3, 6, 5, 3]
    assert actual == expected

def test_insert_before_middle():
    ll.insert_before(4, 7)
    actual = ll.toString()
    expected = [2, 5, 4, 7, 3, 6, 5, 3]
    assert actual == expected

def test_insert_after():
    ll.insert_after(2,1)
    actual = ll.toString()
    expected = [2, 5, 1, 4, 7, 3, 6, 5, 3]
    assert actual == expected

def test_append_multi_values():
    ll.append(2)
    ll.append(3)
    actual = ll.toString()
    expected = [2, 5, 1, 4, 7, 3, 6, 5, 3, 2, 3]
    assert actual == expected

def test_insert_after_middle():
    ll.insert_after(5,1)
    actual = ll.toString()
    expected = [2, 5, 1, 4, 7, 1, 3, 6, 5, 3, 2, 3]
    assert actual == expected

def test_insert_after_last():
    ll.insert_after(12,8)
    actual = ll.toString()
    expected = [2, 5, 1, 4, 7, 1, 3, 6, 5, 3, 2, 3, 8]
    assert actual == expected

def test_kth_is_greater_than_length():
    actual = ll.kth_from_end(13)
    expected = "Value not found"
    assert actual == expected

def test_kth_where_k_is_negative():
    actual = ll.kth_from_end(-1)
    expected = "Negative index"
    assert actual == expected


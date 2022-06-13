import pytest
from linked_list.linkedlist import (
Node,
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

def test_insert_multi():
    ll.insert(5)
    ll.insert(6)
    actual = ll.toString()
    expected = [6, 5, 3]
    assert actual == expected

def test_includes():
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    actual = ll.includes(5)
    expected = True
    assert actual == expected

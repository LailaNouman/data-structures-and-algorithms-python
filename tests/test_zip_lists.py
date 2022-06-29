import pytest
from linked_list.linkedlist import (
LinkedList
)
from zip_lists.zip_lists import (
zip_lists
)

ll1 = LinkedList()
ll1.append(1)
ll1.append(2)
ll1.toString()
ll2 = LinkedList()
ll2.append(3)
ll2.append(4)
ll2.toString()

def test_list1_and_list2_are_equal():
    actual = zip_lists(ll1, ll2)
    expected = [1, 3, 2, 4]
    # assert zip_lists.value == 1
    assert actual == expected

ll3 = LinkedList()
ll3.append(1)
ll3.toString()
ll4 = LinkedList()
ll4.append(3)
ll4.append(4)
ll4.toString()

def test_list3_is_smaller_than_list4():
    actual = zip_lists(ll3, ll4)
    expected = [1, 3, 4]
    assert actual == expected

ll5 = LinkedList()
ll5.append(1)
ll5.append(2)
ll5.toString()
ll6 = LinkedList()
ll6.append(3)
ll6.toString()

def test_list6_is_smaller_than_list5():
    actual = zip_lists(ll5, ll6)
    expected = [1, 3, 2]
    assert actual == expected


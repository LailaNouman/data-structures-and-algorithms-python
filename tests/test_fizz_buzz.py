import pytest
from fizz_buzz.tree_fizz_buzz import TNode, KaryTree, fizz_buzz_tree

k_t = KaryTree()

def test_empty_tree():
    actual = fizz_buzz_tree(k_t)
    expected = None
    assert actual == expected

k_tree = KaryTree()
k_tree.root = TNode(1)

def test_a_single_root():
    actual = fizz_buzz_tree(k_tree)
    expected = [1]
    assert actual == expected

k_tree1 = KaryTree()
k_tree1.root = TNode(15)

def test_a_single_root_with_divisble_number():
    actual = fizz_buzz_tree(k_tree1)
    expected = ['FizzBuzz']
    assert actual == expected

k_tree2 = KaryTree()
k_tree2.root = TNode(1)
k_tree2.root.child.append(TNode(2))
k_tree2.root.child.append(TNode(3))
k_tree2.root.child.append(TNode(4))
k_tree2.root.child.append(TNode(5))
k_tree2.root.child.append(TNode(15))

def test_fizz_buzz_with_multiple_numbers():
    actual = fizz_buzz_tree(k_tree2)
    expected = [2, 'Fizz', 4, 'Buzz', 1, 'FizzBuzz']
    assert actual == expected



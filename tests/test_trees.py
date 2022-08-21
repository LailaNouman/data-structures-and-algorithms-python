import pytest
from trees.tree import Node, BinaryTree, BinarySearchTree

def test_empty_tree():
    tree = BinaryTree()
    actual = tree.root
    expected = None
    assert actual == expected

def test_tree_with_one_root():
    tree = BinaryTree()
    tree.root = Node(1)
    actual = tree.root.value
    expected = 1
    assert actual == expected

tree = BinaryTree()
tree.root = Node("A")
tree.root.left = Node("B")
tree.root.right = Node("C")
tree.root.left.left = Node("D")
tree.root.left.right = Node("E")

def test_pre_order():
    actual = tree.pre_order()
    expected = ['A', 'B', 'D', 'E', 'C']
    assert actual == expected

tree = BinaryTree()
tree.root = Node("A")
tree.root.left = Node("B")
tree.root.right = Node("C")
tree.root.left.left = Node("D")
tree.root.left.right = Node("E")

def test_in_order():
    actual = tree.in_order()
    expected = ['D', 'B', 'E', 'A', 'C']
    assert actual == expected

def test_post_order():
    actual = tree.post_order()
    expected = ['D', 'E', 'B', 'C', 'A']
    assert actual == expected

bTree = BinarySearchTree()
bTree.add(1)
bTree.add(2)
bTree.add(3)
bTree.add(4)
bTree.contains(4)

def test_contains_true():
    actual = bTree.contains(4)
    expected = True
    assert actual == expected

def test_contains_false():
    actual = bTree.contains(5)
    expected = False
    assert actual == expected
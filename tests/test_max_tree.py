import pytest
from trees.tree import Node, BinaryTree

tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(3)
tree.root.right = Node(4)
tree.root.left.left = Node(6)
tree.root.left.right = Node(3)

def test_max_1():
    actual = tree.max_tree()
    expected = 6
    assert actual == expected

tree1 = BinaryTree()
tree1.root = Node(50)
tree1.root.left = Node(30)
tree1.root.right = Node(42)
tree1.root.left.left = Node(63)
tree1.root.left.right = Node(-63)

def test_max_2():
    actual = tree1.max_tree()
    expected = 63
    assert actual == expected
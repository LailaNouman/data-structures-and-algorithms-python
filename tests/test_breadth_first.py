import pytest
from breadth_first.breadth_first import TNode, Tree, breadth_first

tree = Tree()
tree.root = TNode(2)
tree.root.left = TNode(7)
tree.root.right = TNode(5)
tree.root.left.left = TNode(2)
tree.root.left.right = TNode(6)
tree.root.right.left = TNode(9)

def test_breadth_first_case_1():
    actual = breadth_first(tree)
    expected = [2, 7, 5, 2, 6, 9]
    assert actual == expected

tree1 = Tree()
tree1.root = TNode(1)
tree1.root.left = TNode(2)
tree1.root.right = TNode(3)
tree1.root.left.left = TNode(4)
tree1.root.left.right = TNode(5)
tree1.root.right.left = TNode(6)

def test_breadth_first_case_2():
    actual = breadth_first(tree1)
    expected = [1, 2, 3, 4, 5, 6]
    assert actual == expected
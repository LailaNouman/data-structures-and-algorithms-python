from tree_intersection.tree_intersection import BinaryTree, tree_intersection, TreeNode

b1_tree = BinaryTree()
b1_tree.root = TreeNode(100)
b1_tree.root.left = TreeNode(150)
b1_tree.root.left.left = TreeNode(200)
b1_tree.root.left.right = TreeNode(250)
b1_tree.root.left.right.left = TreeNode(300)
b1_tree.root.left.right.right = TreeNode(350)
b1_tree.root.right = TreeNode(400)
b1_tree.root.right.left = TreeNode(450)
b1_tree.root.right.right = TreeNode(500)
b1_tree.root.right.right.left = TreeNode(550)
b1_tree.root.right.right.right = TreeNode(600)
b2_tree = BinaryTree()
b2_tree.root = TreeNode(100)
b2_tree.root.left = TreeNode(15)
b2_tree.root.left.left = TreeNode(20)
b2_tree.root.left.right = TreeNode(50)
b2_tree.root.left.right.left = TreeNode(300)
b2_tree.root.left.right.right = TreeNode(350)
b2_tree.root.right = TreeNode(400)
b2_tree.root.right.left = TreeNode(450)
b2_tree.root.right.right = TreeNode(500)
b2_tree.root.right.right.left = TreeNode(550)
b2_tree.root.right.right.right = TreeNode(600)

def test_tree_intersection1():
    actual = tree_intersection(b1_tree, b2_tree)
    expected = '300, 350, 100, 450, 400, 550, 500, 600'
    assert actual == expected

b3_tree = BinaryTree()
b3_tree.root = TreeNode(100)
b3_tree.root.left = TreeNode(150)
b3_tree.root.left.left = TreeNode(200)
b3_tree.root.left.right = TreeNode(250)
b3_tree.root.left.right.left = TreeNode(300)
b3_tree.root.left.right.right = TreeNode(350)
b3_tree.root.right = TreeNode(400)
b3_tree.root.right.left = TreeNode(450)
b3_tree.root.right.right = TreeNode(500)
b3_tree.root.right.right.left = TreeNode(550)
b3_tree.root.right.right.right = TreeNode(600)
b4_tree = BinaryTree()
b4_tree.root = TreeNode(10)
b4_tree.root.left = TreeNode(15)
b4_tree.root.left.left = TreeNode(20)
b4_tree.root.left.right = TreeNode(50)
b4_tree.root.left.right.left = TreeNode(30)
b4_tree.root.left.right.right = TreeNode(30)
b4_tree.root.right = TreeNode(40)
b4_tree.root.right.left = TreeNode(40)
b4_tree.root.right.right = TreeNode(50)
b4_tree.root.right.right.left = TreeNode(50)
b4_tree.root.right.right.right = TreeNode(60)

def test_tree_intersection2():
    actual = tree_intersection(b3_tree, b4_tree)
    expected = ''
    assert actual == expected


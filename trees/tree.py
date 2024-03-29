class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        if not self.root:
            return self.root
        result = []

        def _walk(root):
            result.append(root.value)
            if root.left:
                _walk(root.left)
            if root.right:
                _walk(root.right)
        _walk(self.root)
        return result

    def in_order(self):
        if not self.root:
            return self.root
        result = []

        def _walk(root):
            if root.left:
                _walk(root.left)
            result.append(root.value)
            if root.right:
                _walk(root.right)
        _walk(self.root)
        return result

    def post_order(self):
        if not self.root:
            return self.root
        result = []

        def _walk(root):
            if root.left:
                _walk(root.left)
            if root.right:
                _walk(root.right)
            result.append(root.value)
        _walk(self.root)
        return result

    def max_tree(self):
        self.max = self.root.value

        def _walk(root):
            if root.value > self.max:
                self.max = root.value
            if root.left:
                _walk(root.left)
            if root.right:
                _walk(root.right)

        _walk(self.root)
        return self.max

class BinarySearchTree(BinaryTree):

    def add(self, value):
        if not self.root:
            self.root = Node(value)

        def _walk(root):
            if value < root.value:
                if root.left:
                    _walk(root.left)
                else:
                    root.left = Node(value)
            elif value > root.value:
                if root.right:
                    _walk(root.right)
                else:
                    root.right = Node(value)
        _walk(self.root)

    def contains(self, search_for):
        if not self.root:
            return False

        def _walk(root):
            if search_for == root.value:
                return True
            else:
                try:
                    if search_for < root.value:
                        return _walk(root.left)
                    elif search_for > root.value:
                        return _walk(root.right)
                except:
                    return False
        if _walk(self.root) == None:
            return False
        else:
            return _walk(self.root)

if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(3)
    tree.root.right = Node(4)
    tree.root.left.left = Node(6)
    tree.root.left.right = Node(3)
    print(tree.pre_order())
    # print(tree.in_order())
    # print(tree.post_order())
    print(tree.max_tree())
    # bTree = BinarySearchTree()
    # bTree.add(1)
    # bTree.add(2)
    # bTree.add(3)
    # bTree.add(4)
    # print(bTree.pre_order())
    # print(bTree.contains(4))

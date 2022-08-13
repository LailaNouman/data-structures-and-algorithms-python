class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class BinaryTree:
    def __init__(self):
        self.root = None

    def in_order(self):
        output = []
        if not self.root:
            return self.root

        def _walk(root, out):

            if root.left:
                _walk(root.left, out)

            out.append(root.value)

            if root.right:
                _walk(root.right, out)

        _walk(self.root, output)
        return output


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node


class HashTable:
    def __init__(self, size=1024):
        self.__size = size
        self.__buckets = [None] * size
        self.__keys_array = []

    def __hash(self, key):
        return sum([ord(i) for i in key]) * 283 % self.__size

    def set(self, key, value):
        hashed_key = self.__hash(key)
        if self.__buckets[hashed_key] is None:
            hash_list = LinkedList()
            self.__buckets[hashed_key] = hash_list
        self.__keys_array.append(key)
        self.__buckets[hashed_key].insert((key, value))

    def get(self, key):
        values = []
        hashed_key = self.__hash(key)
        ll = self.__buckets[hashed_key]
        if ll is None:
            return None

        current = ll.head
        while current:
            if current.value[0] == key:
                values.append(current.value[1])
            current = current.next

        if len(values) > 1:
            return tuple(values)
        else:
            return values[0]

def tree_intersection(tree1, tree2):
    hash_map = HashTable()
    t1 = tree1.in_order()
    t2 = tree2.in_order()
    output = []

    for i in range(len(t1)):
        hash_map.set(str(t1[i]), "0")
        hash_map.set(str(t2[i]), "0")

        if len(hash_map.get(str(t1[i]))) == 2:
            output.append(str(t1[i]))

    return ", ".join(output)


if __name__ == "__main__":
    b1_tree = BinaryTree()
    b2_tree = BinaryTree()

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
    print(tree_intersection(b1_tree, b2_tree))
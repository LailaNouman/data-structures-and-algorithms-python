class EmptyQueueException(Exception):
    pass

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if not self.front:
            raise EmptyQueueException("Empty Queue, you can't dequeue from")
        else:
            temp_node = self.front
            self.front = self.front.next
            return temp_node.value

    def is_empty(self):
        return False if self.front else True

class TNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def breadth_first(self):
        if not self.root:
            return self.root
        result = []
        queue = Queue()
        queue.enqueue(self.root)
        while not queue.is_empty():
            front = queue.dequeue()
            result.append(front.value)
            if front.left:
                queue.enqueue(front.left)
            if front.right:
                queue.enqueue(front.right)
        return result

if __name__ == "__main__":
  tree = Tree()
  tree.root = TNode(2)
  tree.root.left = TNode(7)
  tree.root.right = TNode(5)
  tree.root.left.left = TNode(2)
  tree.root.left.right = TNode(6)
  tree.root.right.left = TNode(9)
  print(tree.breadth_first())
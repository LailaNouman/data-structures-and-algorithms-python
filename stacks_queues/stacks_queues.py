class EmptyStackException(Exception):
    pass
class EmptyQueueException(Exception):
    pass

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if not self.top:
            raise EmptyStackException("You can't pop from an empty stack")

        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.value

    def is_empty(self):
        return True if self.top is None else False

    def peek(self):
        if self.is_empty() == False:
            return self.top.value
        else:
            raise EmptyStackException("EMPTY STACK")

    def __str__(self):
        current = self.top
        items = ''

        while current:
            items += str(current.value) + '\n'
            current = current.next

        return items


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if not self.front:
            raise EmptyQueueException("You can't dequeue from an empty queue")

        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value

    def is_empty(self):
        return True if self.front is None else False

    def peek(self):
        if self.is_empty() == False:
            return self.front.value
        else:
            raise EmptyQueueException("EMPTY QUEUE")

    def __str__(self):
        current = self.front
        items = ''

        while current:
            items += str(current.value) + '\n'
            current = current.next

        return items


if __name__ == "__main__":
    # stack = Stack()
    # stack.push(1)
    # stack.push(2)
    # print(stack)
    # print(stack.pop())
    # print("---------------------")
    queue = Queue()
    queue.enqueue(1)
    # print(queue)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)
    queue.dequeue()
    print(queue)
    print(queue.peek())
    # print(queue.front.value)
    # print(queue.rear.value)



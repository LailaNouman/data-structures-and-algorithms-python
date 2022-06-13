class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def append(self, value):
        newNode = Node(value)
        current_v = self.head
        while True:
            if current_v.next == None:
                current_v.next = newNode
                break
            current_v = current_v.next

    def insert_after(self, index, value):
        self.index = index
        self.value = value
        newNode = Node(value)
        current = self.head
        if index > 1:
            for i in range(1, index):
                current = current.next
            newNode.next = current.next
            current.next = newNode

    def insert_before(self, index, value):
        self.index = index
        self.value = value
        node = Node(value)
        current = self.head
        if index == 1:
            node.next = current
            self.head = node
        else:
            for i in range(1, index - 1):
                current = current.next
            node.next = current.next
            current.next = node

    def toString(self):
        current_v = self.head
        if (current_v != None):
            list = []
            while (current_v != None):
                print("{", current_v.value, end = " } -> ")
                list.append(current_v.value)
                current_v = current_v.next
            print(end = "NULL")
            return list
        else:
            return "Empty list"

    def includes(self, value):
        item = Node(value)
        current = self.head
        if (current.value != item.value):
            while (current.value != item.value):
                current = current.next
            return True
        else:
            return True

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.append(6)
    ll.append(3)
    ll.insert_after(2,4)
    ll.insert_before(2,4)
    str(ll.toString())
    print(ll.head.value)
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

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
        self.__keys = []

    def __hash(self, key):
        return sum([ord(i) for i in key]) * 283 % self.__size

    def set(self, key, value):
        hashed_key = self.__hash(key)
        if self.__buckets[hashed_key] == None:
            hash_list = LinkedList()
            self.__buckets[hashed_key] = hash_list
        self.__keys.append(key)
        self.__buckets[hashed_key].insert((key, value))

    def get(self, key):
        hashed_key = self.__hash(key)
        ll = self.__buckets[hashed_key]
        current = ll.head
        while current:
            if current.value[0] == key:
                return current.value[1]
            current = current.next
        return None

    def contains(self, key):
        idx = self.__hash(key)
        bucket = self.__buckets[idx]
        if bucket is not None:
            current = bucket.head
            while current:
                if current.value[0] == key:
                    return True
                current = current.next
        return False

    def key(self):
        return self.__keys

if __name__ == '__main__':
    hash = HashTable()
    hash.set('Laila', 10)
    # hash.set('Nouman', 20)
    hash.set('Laila', 30)
    print(hash.get('Laila'))
    # print(hash.get('Nouman'))
    print(hash.contains('Nouman'))

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
        self.size = size
        self.buckets = [None] * size
        self.keys = []

    def __hash(self, key):
        hash_key = 0
        for i in key:
          hash_key = hash_key + ord(i)
        hash_key = hash_key * 283
        return hash_key % self.size

    def hash(self, key):
        hash_key = 0
        for i in key:
          hash_key = hash_key + ord(i)
        hash_key = hash_key * 283
        return hash_key % self.size

    def set(self, key, value):
        hashed_key = self.__hash(key)
        if self.buckets[hashed_key] == None:
            hash_list = LinkedList()
            self.buckets[hashed_key] = hash_list
        self.keys.append(key)
        self.buckets[hashed_key].insert((key, value))

    def get(self, key):
        hashed_key = self.__hash(key)
        ll = self.buckets[hashed_key]
        if ll == None:
            return None
        current = ll.head
        while current:
            if current.value[0] == key:
                return current.value[1]
            current = current.next
        return None

    def contains(self, key):
        idx = self.__hash(key)
        bucket = self.buckets[idx]
        if bucket is not None:
            current = bucket.head
            while current:
                if current.value[0] == key:
                    return True
                current = current.next
        return False

    def key(self):
        return self.__keys


def repeated_word(string):
    hash = HashTable()
    split_text = string.lower().replace(',', '').split(' ')
    hash.set(split_text[0], 1)
    for i in range(1, len(split_text)):
        if hash.contains(split_text[i]) is True:
            hashed_key = hash.hash(split_text[i])
            ll = hash.buckets[hashed_key]
            current = ll.head
            while current:
                if current.value[0] == split_text[i]:
                    return current.value[0]
                current = current.next
        else:
            hash.set(split_text[i], 1)

if __name__ == "__main__":
    string = "Once upon a time, there was a brave princess who..."
    print(repeated_word(string))
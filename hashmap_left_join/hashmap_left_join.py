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

    def contains(self, key):
        if self.get(key):
          return True

        return False

    def keys(self):
        return self.__keys_array

def left_join(ht1, ht2):
    output = []

    for i in ht1.keys():
        if i in ht2.keys():
            output.append([i, ht1.get(i), ht2.get(i)])
        else:
            output.append([i, ht1.get(i), "NULL"])

    return output

if __name__ == "__main__":
    hash_table1 = HashTable()
    hash_table1.set("diligent", "employed")
    hash_table1.set("fond", "enamored")
    hash_table1.set("guide", "usher")
    hash_table1.set("outfit", "garb")
    hash_table1.set("wrath", "anger")

    hash_table2 = HashTable()
    hash_table2.set("diligent", "idle")
    hash_table2.set("fond", "averse")
    hash_table2.set("guide", "follow")
    hash_table2.set("flow", "jam")
    hash_table2.set("wrath", "delight")

    print(left_join(hash_table1, hash_table2))
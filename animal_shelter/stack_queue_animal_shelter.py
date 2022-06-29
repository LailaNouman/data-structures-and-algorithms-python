class Node:
    def __init__(self, name, pref):
        self.name = name
        self.pref = pref
        self.next = None


class AnimalShelter:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, name, pref):
        node = Node(name, pref)
        if not self.front:
            self.rear = node
            self.front = self.rear
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self, pref):
        if pref != "cat" and pref != "dog":
            return None
        current = self.front
        while current:
            if current.pref == pref:
                self.front = self.front.next
                return current.name
            elif current.next is not None and current.next.pref == pref:
                temp = current.next.name
                current.next = current.next.next
                return temp
            current = current.next
        print(f"{pref} not found in the queue")

    def __str__(self):
        text = ""
        current = self.front
        while current:
            text = f'{current.pref}: {current.name}, ' + text
            current = current.next
        return text

if __name__ == "__main__":
    shelter = AnimalShelter()
    shelter.enqueue("sherry", "cat")
    shelter.enqueue("alex", "dog")
    shelter.enqueue("simba", "cat")
    shelter.enqueue("night", "dog")
    shelter.enqueue("tom", "cat")
    print(shelter)
    shelter.dequeue("cat")
    print(shelter)
    shelter.dequeue("cat")
    print(shelter)
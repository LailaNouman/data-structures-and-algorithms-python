class EmptyStackException(Exception):
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

def validate_brackets(shape):
    shapes = ["{}", "[]", "()"]
    stack = Stack()
    for bracket in shape:
        if bracket == "{" or bracket == "(" or bracket == "[":
            stack.push(bracket)
        elif bracket == "}" or bracket == ")" or bracket == "]":
            if stack.top is None:
                return False
            elif (stack.top.value + bracket) in shapes:
                stack.pop()
            else:
                return False
    return True if stack.is_empty() else False


if __name__ == "__main__":
    print(validate_brackets("{}"))
    print(validate_brackets("{}(){}"))
    print(validate_brackets("()[True]"))
    print(validate_brackets("(){}[[]]"))
    print(validate_brackets("(]("))
    print(validate_brackets("{(})"))
    print(validate_brackets("{([])}"))
    print(validate_brackets("({})"))
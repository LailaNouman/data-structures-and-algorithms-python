import pytest
from stacks_queues.stacks_queues import Stack, Queue

stack = Stack()
stack.push(1)

def test_pushing_into_stack():
    actual = stack.peek()
    expected = 1
    assert actual == expected

stack2 = Stack()
stack2.push(1)
stack2.push(2)

def test_pushing_multiple_values():
    actual = stack2.peek()
    expected = 2
    assert actual == expected

stack3 = Stack()
stack3.push(1)
stack3.push(2)

def test_pop_from_the_stack():
    actual = stack3.pop()
    expected = 1
    assert actual == expected

stack4 = Stack()

def test_empty_stack():
    actual = stack4.is_empty()
    expected = True
    assert actual == expected

queue = Queue()
queue.enqueue(1)

def test_enqueuing_into_queue():
    actual = queue.peek()
    expected = 1
    assert actual == expected

queue2 = Queue()
queue2.enqueue(1)
queue2.enqueue(2)

def test_enqueuing_multiple_values():
    actual = queue2.peek()
    expected = 1
    assert actual == expected

queue3 = Queue()
queue3.enqueue(1)
queue3.enqueue(2)

def test_dequeue():
    actual = queue3.dequeue()
    expected = 2
    assert actual == expected

def test_peeking_queue():
    queue.enqueue(1)
    queue.enqueue(2)
    actual = queue.peek()
    expected = 1
    assert actual == expected

queue4 = Queue()

def test_empty_queue():
    actual = queue4.is_empty()
    expected = True
    assert actual == expected


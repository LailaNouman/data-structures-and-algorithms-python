import pytest
from stacks_queues.stacks_queues import Stack, PseudoQueue

q = PseudoQueue()
q.enqueue(1)

def test_enqueue():
    actual = q
    expected = 1
    assert actual == expected

q1 = PseudoQueue()
q1.enqueue(1)
q1.enqueue(2)
q1.dequeue()

def test_dequeue():
    actual = q1
    expected = 2
    assert actual == expected

q2 = PseudoQueue()
q2.enqueue(1)
q2.enqueue(2)
q2.enqueue(3)
q2.dequeue()
q2.dequeue()

def test_dequeue_multiple_values():
    actual = q2
    expected = 3
    assert actual == expected


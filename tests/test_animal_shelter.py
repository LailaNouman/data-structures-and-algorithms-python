import pytest
from animal-shelter.stack_queue_animal_shelter import AnimalShelter

q = AnimalShelter()
q.enqueue("sherry", "cat")
q.enqueue("alex", "dog")
q.enqueue("simba", "cat")
q.enqueue("night", "dog")

def test_queue_case1():
    actual = q.front.name
    expected = "sherry"
    assert actual == expected

def test_queue_case2():
    actual = q.rear.name
    expected = "night"
    assert actual == expected

def test_dequeue_case1():
    actual = q.dequeue("cat")
    expected = "sherry"
    assert actual == expected

def test_dequeue_case2():
    actual = q.dequeue("dog")
    expected = "alex"
    assert actual == expected

def test_dequeue_case3():
    actual = q.dequeue("dog")
    expected = "night"
    assert actual == expected



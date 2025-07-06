import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from stack import Stack


def test_new_stack_is_empty():
    stack = Stack()
    assert stack.peek() is None
    assert stack.pop() is None


def test_push_and_pop_single_item():
    stack = Stack()
    stack.push(5)
    assert stack.peek() == 5
    assert stack.pop() == 5
    assert stack.peek() is None


def test_push_multiple_items():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.peek() == 3
    assert stack.pop() == 3
    assert stack.peek() == 2
    assert stack.pop() == 2
    assert stack.peek() == 1
    assert stack.pop() == 1


def test_stack_length():
    stack = Stack()
    assert len(stack) == 0
    stack.push(1)
    assert len(stack) == 1
    stack.pop()
    assert len(stack) == 0

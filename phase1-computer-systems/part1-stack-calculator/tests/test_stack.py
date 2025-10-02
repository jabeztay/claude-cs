import pytest
from stack import Stack, EmptyStackError


def test_push():
    """Test pushing an item onto the stack."""
    stack = Stack()
    stack.push(42)
    assert stack.peek() == 42
    assert stack.size() == 1


def test_pop():
    """Test popping an item from the stack."""
    stack = Stack()
    stack.push(42)
    item = stack.pop()
    assert item == 42
    assert stack.size() == 0


def test_peek():
    """Test peeking does not remove the item from top of stack."""
    stack = Stack()
    stack.push(42)
    item = stack.peek()
    assert item == 42
    assert stack.size() == 1


def test_pop_empty():
    """Test popping from an empty stack raises EmptyStackError."""
    stack = Stack()
    with pytest.raises(EmptyStackError):
        stack.pop()


def test_peek_empty():
    """Test peeking into an empty stack raises EmptyStackError."""
    stack = Stack()
    with pytest.raises(EmptyStackError):
        stack.peek()


def test_multiple_operations():
    """Test a sequence of push, pop, and peek operations."""
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.peek() == 3
    assert stack.pop() == 3
    assert stack.peek() == 2
    assert stack.size() == 2
    stack.push(4)
    assert stack.peek() == 4
    assert stack.size() == 3


def test_is_empty_new_stack():
    """Test that a new stack is empty."""
    stack = Stack()
    assert stack.size() == 0
    assert stack.is_empty()


def test_is_empty_after_pops():
    """Test that the stack is empty after popping all items."""
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.pop()
    stack.pop()
    assert stack.size() == 0
    assert stack.is_empty()


def test_size():
    """Test the size method of the stack."""
    stack = Stack()
    assert stack.size() == 0
    stack.push(1)
    assert stack.size() == 1
    stack.push(2)
    assert stack.size() == 2
    stack.pop()
    assert stack.size() == 1
    stack.pop()
    assert stack.size() == 0


def test_peek_then_pop():
    """Test that peek followed by pop returns the same item."""
    stack = Stack()
    stack.push(42)
    assert stack.peek() == 42
    assert stack.pop() == 42
    assert stack.size() == 0


def test_repr():
    """Test the string representation of the stack."""
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert repr(stack) == "Stack([1, 2])"
    stack.pop()
    assert repr(stack) == "Stack([1])"
    stack.pop()
    assert repr(stack) == "Stack([])"

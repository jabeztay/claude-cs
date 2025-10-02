from typing import Any


class EmptyStackError(Exception):
    """Raised when attempting to pop or peek from an empty stack."""

    pass


class Stack:
    """A simple stack implementation using a Python list."""

    def __init__(self) -> None:
        self._items = []

    def push(self, item: Any) -> None:
        """Push an item onto the stack."""
        self._items.append(item)

    def peek(self) -> Any:
        """Return the top item of the stack without removing it."""
        if self.is_empty():
            raise EmptyStackError("Cannot peek from an empty stack.")
        return self._items[-1]

    def pop(self) -> Any:
        """Remove and return the top item of the stack."""
        if self.is_empty():
            raise EmptyStackError("Cannot pop from an empty stack.")
        return self._items.pop()

    def size(self) -> int:
        """Return the number of items in the stack."""
        return len(self._items)

    def is_empty(self) -> bool:
        """Return True if the stack is empty, False otherwise."""
        return not self._items

    def __repr__(self) -> str:
        return f"Stack({self._items})"

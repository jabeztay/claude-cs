from typing import Any

class Stack:
    def __init__(self):
        self._stack = []

    def push(self, value: Any):
        self._stack.append(value)

    def pop(self):
        if self._stack:
            return self._stack.pop()
        return None

    def peek(self):
        if self._stack:
            return self._stack[-1]
        return None

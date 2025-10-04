# Stack Calculator

## Overview

A postfix notation calculator built to understand stack data structures and expression evaluation.

## What is Postfix Notation?

Instead of writing `3 + 4`, postfix notation writes `3 4 +`. This eliminates the need for parentheses and makes evaluation straightforward using a stack.

Examples:
- Infix: `(3 + 4) * 2` → Postfix: `3 4 + 2 *`
- Infix: `3 + (4 * 2)` → Postfix: `3 4 2 * +`

## Design Decisions

### Stack Implementation
- A custom class wrapping around Python list for learning. In production environments, using `collections.deque` is preferred for efficiency.
- Can hold any data type
- Raises `EmptyStackError` on invalid pop/peeks on empty stack

### Core Operations
- `push(item)`: add item to the top of the stack
- `pop()`: remove and return the top item from the stack
- `peek()`: return the top item from the stack without removing it
- `is_empty()`: return True if the stack is empty, False otherwise
- `size()`: return the number of items in the stack
- `__repr__()`: return a string representation of the stack for debugging purposes 

## Features

### Core
- [x] Basic stack implementation (push, pop, peek)
- [x] Postfix expression evaluator
- [x] Support for `+`, `-`, `*`, `/` operations
- [x] Error handling for invalid expressions
- [x] Constants like `pi` and `e`

### Extensions
- [ ] Variable storage and retrieval
- [ ] Mathematical functions (sin, cos, sqrt, pow)
- [ ] Expression validation

## Usage

```python
# Example usage (to be implemented)
calc = Calculator()
result = calc.evaluate("3 4 + 2 *")  # Returns 14
```

## Project Structure

```
part1-stack-calculator/
├── src/
│   ├── stack.py        # Stack data structure
│   ├── calculator.py   # Main calculator logic
│   └── tokenizer.py    # Expression tokenization
├── tests/
│   ├── test_stack.py
│   ├── test_calculator.py
│   └── test_tokenizer.py
├── examples/
│   └── demo.py         # Usage examples
└── README.md           # This file
```

## Testing

```bash
# Run tests
pytest tests/

# Run with coverage
pytest tests/ --cov=src
```

## Learning Goals

- Understand stack operations deeply
- See why postfix notation simplifies evaluation
- Practice test-driven development
- Build foundation for VM implementation

## References

- [Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation)
- [Shunting Yard Algorithm](https://en.wikipedia.org/wiki/Shunting_yard_algorithm) (for infix to postfix conversion)

---

*This is a personal learning repository. The code here prioritizes understanding over production readiness.*

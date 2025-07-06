# Simple Virtual Machine

**Duration:** Week 3-4 (14 days)  
**Phase:** Computer Systems Fundamentals

## Learning Objectives
- Understand instruction sets and opcodes
- Learn about registers vs stack-based architectures
- Grasp memory organization

## Project Goal
Build a VM that executes bytecode instructions

## VM Design
Instruction Set:
```python
LOAD_CONST = 1    # Load constant onto stack
ADD = 2           # Pop two values, add, push result
SUB = 3           # Pop two values, subtract, push result
MUL = 4           # Pop two values, multiply, push result
STORE = 5         # Store top of stack to variable
LOAD_VAR = 6      # Load variable onto stack
PRINT = 7         # Print top of stack
HALT = 8          # Stop execution
```

## Implementation Features
- Stack-based architecture
- Bytecode instruction execution
- Memory management for variables
- Basic I/O operations

## Code Structure
```
virtual-machine/
├── vm.py            # Virtual machine implementation
├── instructions.py  # Instruction definitions
├── memory.py       # Memory management
├── assembler.py    # Bytecode generation utilities
├── main.py         # VM runner
└── tests/          # Unit tests
```

## Deliverable
Virtual machine that can execute bytecode programs with:
- Stack-based computation
- Variable storage and retrieval
- Basic arithmetic operations
- Program flow control
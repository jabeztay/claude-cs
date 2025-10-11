# Virtual Machine

## Overview

A stack-based virtual machine with bytecode instruction set, memory management, and control flow. Built to understand how programs execute at a low level.

## What is a Virtual Machine?

A virtual machine (VM) is an emulation of a computer system that provides an abstraction layer between hardware and software. Programs compiled to the VM's bytecode can run on any platform that has a compatible VM implementation, making them portable across different hardware architectures.

**Real-world examples:** Java Virtual Machine (JVM), Python's CPython VM, WebAssembly runtime

## Connection to Stack Calculator

The VM builds directly on concepts from Part 1:

- **Reuses the Stack class** built in Part 1 for the execution stack
- **Stack operations** like PUSH/POP are now bytecode instructions
- **Arithmetic operations** (ADD, SUB, etc.) from the calculator become VM opcodes
- **Key difference:** The calculator evaluated postfix expressions directly; the VM executes lower-level bytecode instructions, enabling loops, conditionals, and memory storage

## Design Decisions

### Architecture Components

**1. Instruction Set (Bytecode)**
- Each instruction has a numeric opcode (e.g., `PUSH = 0x01`)
- Instructions are stored as a sequence of bytes
- Some instructions take operands (e.g., `PUSH 5`), others don't (e.g., `ADD`)

**2. Execution Stack**
- Uses the Stack class from Part 1
- Stores intermediate values during computation
- Operations pop operands from stack, push results back

**3. Memory Array**
- Separate from the stack
- Indexed storage for variables (e.g., memory[0], memory[1])
- Accessed via `LOAD` and `STORE` instructions

**4. Program Counter (PC)**
- Tracks current instruction position
- Increments after each instruction
- Modified by jump instructions for control flow

### Instruction Set

**Stack Operations**
- `PUSH <value>` - Push a value onto the stack
- `POP` - Remove top value from stack
- `DUP` - Duplicate top stack value
- `SWAP` - Swap top two stack values

**Arithmetic Operations**
- `ADD` - Pop two values, push their sum
- `SUB` - Pop two values, push their difference
- `MUL` - Pop two values, push their product
- `DIV` - Pop two values, push their quotient

**Comparison Operations**
All comparison operations pop two values, compare them, and push 1 (true) or 0 (false):
- `EQ` - Equal to
- `NEQ` - Not equal to
- `LT` - Less than
- `GT` - Greater than
- `LE` - Less than or equal
- `GE` - Greater than or equal

**Control Flow**
- `JMP <address>` - Unconditional jump to address
- `JZ <address>` - Jump if top of stack is zero
- `JNZ <address>` - Jump if top of stack is non-zero

**Memory Access**
- `LOAD <address>` - Push value from memory[address] to stack
- `STORE <address>` - Pop value from stack, store in memory[address]

**I/O and Control**
- `PRINT` - Pop and print top of stack value
- `HALT` - Stop execution

### Bytecode Format

Instructions are represented as lists of integers:
```python
# Example: Push 5, Push 3, Add, Print, Halt
# For readability, using an enum for opcodes
bytecode = [
    Opcode.PUSH.value, 5,
    Opcode.PUSH.value, 3,
    Opcode.ADD.value,
    Opcode.PRINT.value,
    Opcode.HALT.value
]
```

## Features

### Core
- [x] Instruction set implementation
- [x] Stack-based execution engine
- [x] Program counter and execution loop
- [x] Memory array for variable storage
- [x] Arithmetic operations (ADD, SUB, MUL, DIV)
- [x] Comparison operations (EQ, NEQ, LT, GT, LE, GE)
- [x] Control flow (jumps, conditionals)
- [x] Basic I/O (PRINT)

### Extensions
- [ ] Function calls (CALL/RET with call stack)
- [ ] Debugging mode (step-through execution)
- [x] Bytecode disassembler (convert bytes to readable format)
- [ ] Execution tracing and profiling
- [ ] Error handling and stack overflow protection

## Usage

```python
# Example: Calculate 5 + 3 and print result
vm = VirtualMachine(memory_size=256)

bytecode = [
    Opcode.PUSH.value, 5,
    Opcode.PUSH.value, 3,
    Opcode.ADD.value,
    Opcode.PRINT.value,
    Opcode.HALT.value
]

vm.run(bytecode)  # Output: 8

# Example: Loop from 0 to 5
bytecode = [
    Opcode.PUSH.value, 0,        # counter starts at 0
    Opcode.DUP.value,            # duplicate for comparison
    Opcode.PUSH.value, 5,        # push limit
    Opcode.GE.value,             # counter >= 5?
    Opcode.JNZ.value, 14,        # if true, jump to HALT
    Opcode.PUSH.value, 1,        # push 1
    Opcode.ADD.value,            # increment counter
    Opcode.JMP.value, 1,         # jump back to DUP
    Opcode.HALT.value            # end program
]

vm.run(bytecode)
```

## Examples

See `examples/demo.py` for complete working programs:
- Factorial calculation (5! = 120)
- Fibonacci sequence (first N numbers)

Use the disassembler to view bytecode in readable format:
```python
from disassembler import disassemble
bytecode = factorial(5)
print(disassemble(bytecode))
```

## Project Structure

```
part2-virtual-machine/
├── src/
│   ├── vm.py           # Virtual machine implementation
│   ├── opcodes.py      # Opcode definitions and constants
│   └── assembler.py    # Text assembly to bytecode (optional)
├── tests/
│   ├── test_vm.py
│   ├── test_opcodes.py
│   └── test_programs/  # Example bytecode programs
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

# Test specific programs
python -m pytest tests/test_programs/
```

## Learning Goals

- Understand bytecode execution and instruction sets
- Implement fetch-decode-execute cycle
- See how high-level concepts (loops, variables) map to low-level instructions
- Build foundation for compiler in Part 3
- Grasp the relationship between VMs, assembly, and machine code

## Key Concepts

**Fetch-Decode-Execute Cycle:**
1. **Fetch:** Read instruction at program counter
2. **Decode:** Determine what operation to perform
3. **Execute:** Perform the operation
4. **Repeat:** Increment PC and continue (unless HALT or JUMP)

**Why Stack-Based?**
- Simpler instruction set (no need to specify registers)
- Easy to implement
- Natural fit for expression evaluation
- Foundation for understanding other VM architectures

**Bytecode vs Assembly vs Machine Code:**
- **Bytecode:** VM-specific instructions (what you're building)
- **Assembly:** Human-readable mnemonics for machine code (e.g., x86 assembly)
- **Machine Code:** Native CPU instructions (what hardware executes)

## References

### Virtual Machine Design
- [Crafting Interpreters - Bytecode Virtual Machines](https://craftinginterpreters.com/a-bytecode-virtual-machine.html)
- [Write your Own Virtual Machine](https://justinmeiners.github.io/lc3-vm/)
- [Stack-based vs Register-based VMs](https://docs.oracle.com/javase/specs/jvms/se7/html/jvms-2.html)

### Instruction Set Architecture
- [JVM Instruction Set](https://docs.oracle.com/javase/specs/jvms/se7/html/jvms-6.html)
- [Python Bytecode](https://docs.python.org/3/library/dis.html)
- [WebAssembly Core Specification](https://webassembly.github.io/spec/core/)

### Implementation Guides
- [Building a Virtual Machine in Python](https://csl.name/post/vm/)
- [Let's Build a Simple Interpreter (Series)](https://ruslanspivak.com/lsbasi-part1/)

---

*This is a personal learning repository. The code here prioritizes understanding over production readiness.*

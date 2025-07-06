# Simple Language Compiler

**Duration:** Week 5-6 (14 days)  
**Phase:** Computer Systems Fundamentals

## Learning Objectives
- Understand compilation vs interpretation
- Learn lexical analysis and parsing
- Connect high-level syntax to low-level instructions

## Project Goal
Build a compiler for a simple language that targets your VM

## Language Syntax
Your language should handle:
```javascript
// Basic operations
let x = 10 + 5;
let y = x * 2;
print(y);

// Control flow
if (x > 5) {
    print("x is big");
}
```

## Implementation Components
1. **Lexical Analysis:** Break source code into tokens
2. **Parsing:** Build Abstract Syntax Tree (AST)
3. **Code Generation:** Convert AST to VM bytecode
4. **Optimization:** Basic optimizations (optional)

## Code Structure
```
simple-language-compiler/
├── lexer.py         # Tokenization
├── parser.py        # AST generation
├── ast_nodes.py     # AST node definitions
├── compiler.py      # Code generation
├── main.py          # Compiler driver
├── examples/        # Sample programs
└── tests/           # Unit tests
```

## Language Features
- Variable declarations and assignments
- Arithmetic expressions
- Basic control flow (if statements)
- Print statements
- Type checking (basic)

## Deliverable
Compiler that translates high-level language to VM bytecode:
- Lexical analysis of source code
- Syntax parsing with error reporting
- AST-based code generation
- Integration with Phase 1 VM
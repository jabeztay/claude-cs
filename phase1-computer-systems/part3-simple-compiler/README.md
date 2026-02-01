# Simple Compiler

## Overview

A compiler for a minimal programming language that targets the stack-based VM from Part 2. Built to understand how high-level code transforms into executable bytecode.

## What is a Compiler?

A compiler translates source code written in a high-level language into lower-level instructions that a machine (or virtual machine) can execute. This compiler bridges human-readable code to the bytecode format our VM understands.

**Pipeline:** `source code → tokens → AST → bytecode`

## Connection to Previous Parts

This compiler builds directly on Parts 1 and 2:

- **From Stack Calculator (Part 1):** Tokenization concepts, expression evaluation patterns
- **From Virtual Machine (Part 2):** Target instruction set - the compiler generates bytecode the VM executes
- **Key insight:** Post-order AST traversal for code generation mirrors postfix evaluation

## Language Design

### Syntax (Brace-based, Python-inspired)

```
i = 1
while i < 6 {
    print(i)
    i = i + 1
}
```

### Supported Features

- Variable assignment (`x = 5`)
- Arithmetic expressions (`x + y * 2`)
- Comparison operators (`<`, `>`, `<=`, `>=`, `==`, `!=`)
- `while` loops
- `if`/`else` conditionals
- `print` statement

### Design Decisions

- **Brace-based blocks:** Simpler than indentation-based (no INDENT/DEDENT tokens needed)
- **Simple operators only:** No compound assignment (`+=`), use `x = x + 1`
- **Integers only:** No floats for simplicity
- **No functions:** Would require CALL/RET instructions and call stack in VM

## Compiler Architecture

### Stage 1: Lexer (Tokenizer)
Converts source code string into a sequence of tokens.

**Input:** `"i = 1"`
**Output:** `[Token(IDENTIFIER, "i"), Token(ASSIGN, "="), Token(NUMBER, 1)]`

### Stage 2: Parser
Converts token sequence into an Abstract Syntax Tree (AST).

**Input:** Tokens for `i = i + 1`
**Output:**
```
Assignment
├── target: Identifier("i")
└── value: BinaryOp(+)
           ├── left: Identifier("i")
           └── right: Number(1)
```

### Stage 3: Code Generator
Walks the AST and emits bytecode instructions.

**Input:** AST for `i = i + 1`
**Output:**
```
LOAD i      ; load variable i onto stack
PUSH 1      ; push literal 1
ADD         ; pop two values, push sum
STORE i     ; pop and store into variable i
```

## Token Types

```
Keywords:       WHILE, IF, ELSE, PRINT
Operators:      PLUS, MINUS, STAR, SLASH
                LT, GT, LE, GE, EQ, NEQ
                ASSIGN
Literals:       NUMBER
Identifiers:    IDENTIFIER
Delimiters:     LBRACE, RBRACE, LPAREN, RPAREN
End:            EOF
```

### Lexer Design Notes

- **Lookahead required:** To distinguish `=` vs `==`, `<` vs `<=`, etc.
- **Keyword detection:** Lex as identifier first, then check against keyword list
- **Whitespace:** Ignored (braces define structure, not indentation)

## Bytecode Generation Patterns

### Assignment: `x = expr`
1. Generate code for `expr` (leaves value on stack)
2. Emit `STORE x`

### Binary Operation: `a + b`
1. Generate code for left operand
2. Generate code for right operand
3. Emit operator instruction (`ADD`, `SUB`, etc.)

This is **post-order traversal** - process children before the node itself.

### While Loop: `while cond { body }`
```
LOOP_START: <condition code>    ; leaves 0 or 1 on stack
            JZ LOOP_END         ; exit if condition false
            <body code>
            JMP LOOP_START      ; repeat
LOOP_END:   ...
```

### Example: Complete Program

Source:
```
i = 1
while i < 6 {
    print(i)
    i = i + 1
}
```

Bytecode:
```
PUSH 1
STORE i
LOOP_START: PUSH 6
            LOAD i
            GE
            JNZ EXIT
            LOAD i
            PRINT
            LOAD i
            PUSH 1
            ADD
            STORE i
            JMP LOOP_START
EXIT:       HALT
```

## Project Structure

```
part3-simple-compiler/
├── src/
│   ├── tokens.py       # Token and TokenType definitions
│   ├── lexer.py        # Lexer implementation
│   ├── ast_nodes.py    # AST node definitions
│   ├── parser.py       # Parser implementation
│   └── codegen.py      # Bytecode generator
├── tests/
│   ├── test_lexer.py
│   ├── test_parser.py
│   └── test_codegen.py
├── examples/
│   └── demo.py         # End-to-end examples
└── README.md           # This file
```

## Development Plan

### Phase 1: Lexer
1. Implement TokenType enum and Token dataclass
2. Handle numbers and basic operators (`+`, `-`, `*`, `/`)
3. Add comparison operators with lookahead (`==`, `<=`, etc.)
4. Add identifiers and keywords
5. Add delimiters (`{`, `}`, `(`, `)`)

**Test with:** Simple expressions like `1 + 2`, then `x = 1`

### Phase 2: Parser
1. Define AST node classes
2. Parse expressions (handle operator precedence)
3. Parse assignment statements
4. Parse `print` statements
5. Parse `while` loops
6. Parse `if`/`else` conditionals

### Phase 3: Code Generator
1. Generate code for literals and identifiers
2. Generate code for binary operations
3. Generate code for assignments
4. Generate code for `print`
5. Generate code for `while` (requires label/address resolution)
6. Generate code for `if`/`else`

### Phase 4: Integration
1. Connect lexer → parser → codegen pipeline
2. Run generated bytecode on VM from Part 2
3. End-to-end testing

## Testing

```bash
# Run tests
pytest tests/

# Run with coverage
pytest tests/ --cov=src
```

## Learning Goals

- Understand the compilation pipeline (lex → parse → codegen)
- Implement tokenization with lookahead
- Build recursive descent parser
- See how high-level constructs map to low-level bytecode
- Connect theory (AST traversal) to practice (code generation)

## Key Concepts

**Lexer/Tokenizer:** Breaks source into tokens. Handles lookahead for multi-character operators. Distinguishes keywords from identifiers.

**Parser:** Builds tree structure from flat token sequence. Must handle operator precedence. Uses recursive descent approach.

**Code Generator:** Walks AST in post-order. Emits bytecode for each node. Resolves jump addresses for control flow.

**AST (Abstract Syntax Tree):** Hierarchical representation of program structure. Captures what operations to perform without syntax details (no braces, parentheses in tree - just structure).

## References

- [Crafting Interpreters - Scanning](https://craftinginterpreters.com/scanning.html)
- [Crafting Interpreters - Parsing Expressions](https://craftinginterpreters.com/parsing-expressions.html)
- [Crafting Interpreters - Compiling Expressions](https://craftinginterpreters.com/compiling-expressions.html)
- [Let's Build a Simple Interpreter](https://ruslanspivak.com/lsbasi-part1/)

## Extensions (Future)

- [ ] Error reporting with line numbers
- [ ] `for` loops
- [ ] Logical operators (`and`, `or`, `not`)
- [ ] Functions (requires VM extensions: CALL, RET, call stack)
- [ ] String literals
- [ ] Comments

---

## Current Status: Paused for Crafting Interpreters

**Date Paused:** 2025-02-01

### Why the Detour?

After designing the compiler architecture and understanding how constructs map to bytecode, it became clear that a more structured reference would accelerate learning. [Crafting Interpreters](https://craftinginterpreters.com/) provides battle-tested patterns for:

- Precedence parsing (handling `1 + 2 * 3` correctly)
- Error handling and recovery
- Complete language implementation from scratch

### The Plan

1. Work through Crafting Interpreters Part II (Tree-Walk Interpreter)
2. Build Lox (or significant portions) as a learning exercise
3. Return to this compiler with deeper understanding
4. Potentially redesign VM instruction set based on learnings
5. Complete this compiler targeting the improved VM

### What's Been Established

- Compilation pipeline: `source → tokens → AST → bytecode`
- Token types needed for the language
- How assignment, loops, and conditionals map to bytecode
- Post-order AST traversal for code generation
- Lookahead for multi-character operators

### Questions to Explore During Detour

- How does Lox handle operator precedence? (Pratt parsing vs recursive descent)
- What VM design decisions does clox make differently?
- How are variables scoped and resolved?
- How does error recovery work in the parser?

### Notes to Capture While Reading

Keep track of:
- Design decisions that differ from our VM
- "Aha" moments about parsing or code generation
- Things our instruction set can't handle
- Ideas for improving the VM

---

*This is Part 3 of a personal CS learning repository. The code prioritizes understanding over production readiness.*
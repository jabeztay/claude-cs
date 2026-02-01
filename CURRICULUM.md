# Computer Science Fundamentals Curriculum

## Overview

A self-paced journey through CS fundamentals via practical implementation. Each phase answers a core question about computing.

## Phase 1: Computer Systems Fundamentals

**Core Question**: How do computers execute programs?

### Part 1: Stack Calculator ✓
- **Goal**: Understand stack data structures and expression evaluation
- **Build**: Postfix notation calculator
- **Learn**: Stack operations, parsing, evaluation strategies
- **Foundation for**: VM's execution stack

### Part 2: Virtual Machine ✓
- **Goal**: Understand how programs execute as bytecode
- **Build**: Stack-based VM with instruction set
- **Learn**: Opcodes, program counter, execution loop
- **Foundation for**: Understanding compilation targets

### Part 3: Simple Compiler (In Progress)
- **Goal**: Bridge high-level code to VM bytecode
- **Build**: Compiler for a minimal language
- **Learn**: Lexing, parsing, AST, code generation
- **Foundation for**: Understanding how languages work

#### Crafting Interpreters Detour (Current)

Before completing the compiler, taking a structured detour through [Crafting Interpreters](https://craftinginterpreters.com/) to build stronger foundations in:

- Precedence parsing (Pratt parsing vs recursive descent)
- Error handling and recovery
- Complete language implementation patterns

**Path:**
1. Work through Part II: Tree-Walk Interpreter (Chapters 4-13)
2. Optionally explore Part III: Bytecode Virtual Machine
3. Return to complete Part 3 compiler with deeper understanding
4. Consider redesigning VM based on learnings

**Why this approach:** The design phase revealed that parser construction (especially precedence handling) benefits from a complete reference implementation. Building Lox provides that foundation while still being hands-on learning.

### Potential Extensions
- Debugger for the VM
- Optimizer for the compiler
- Additional language features (functions, closures)
- Redesign VM instruction set based on Crafting Interpreters learnings

## Phase 2: Data Structures in Practice

**Core Question**: How do we organize data efficiently?

### Planned Concepts
- Hash tables with collision resolution
- B-trees for ordered data
- Persistent storage mechanisms
- Build towards: Key-value store

*Details to be determined based on Phase 1 learnings*

## Phase 3: Database Internals

**Core Question**: How do databases actually work?

### Planned Concepts
- Storage engines and page management
- Query processing and optimization
- Indexing strategies
- Transaction management
- Build towards: Mini database engine

*Details to be determined based on Phase 2 learnings*

## Phase 4: Distributed Systems

**Core Question**: How do we scale beyond one machine?

### Planned Concepts
- Network communication and RPC
- Consensus algorithms (Raft)
- Fault tolerance and failover
- Partitioning and load balancing
- Build towards: Distributed key-value store

*Details to be determined based on Phase 3 learnings*

## Learning Principles

1. **Iterative Planning**: Detail each part after completing the previous
2. **Connection Over Isolation**: Each concept builds on prior work
3. **Depth Over Breadth**: Better to deeply understand fewer concepts
4. **Reflection Required**: Document learnings before moving forward
5. **Detours Are Valid**: Following references like Crafting Interpreters when they serve learning goals

## Success Metrics

Not about completion speed, but about:
- Can explain each concept clearly
- Code demonstrates understanding
- Can identify trade-offs in design decisions
- Can connect concepts to real-world systems

## How This Curriculum Evolves

After completing each part:
1. Review what was learned
2. Identify areas needing more exploration
3. Adjust next part's scope and depth accordingly
4. Update this document with specifics

## Current Focus

**Active**: Phase 1, Part 3 - Simple Compiler (Crafting Interpreters detour)
**Next**: Complete Part 3 compiler, then Phase 2
**Adjustments**: Crafting Interpreters added as structured foundation for compiler work
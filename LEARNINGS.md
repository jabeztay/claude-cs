# Learning Journal

## Phase 1: Computer Systems

### Part 1: Stack Calculator

**Date Started**: 2025-10-01
**Date Completed**: 2025-10-05

#### Key Concepts Learned

- Test Driven Development with pytest
- Stacks and postfix evaluation

#### Challenges Faced

- First time actually doing TDD. Writing tests initially was weird. Also setting up pytest to work initially was a bit confusing due to paths.
- Variable storage and retrieval. Especially the part on storing, since it doesn't entirely tie into postfix evaluation.

#### Breakthrough Moments

- Realising that storage of variables just does not fit into postfix evaluation nicely.

#### Connections to Other Concepts

- Passing context around, like variable storage, or the last result, is similar to how context of processing an event in stream processing systems is passed. We can use it to manage state, or pass data/metadata across different stages of the whole processing pipeline.
- Tokenization is an important part of many systems. We need to break down input into manageable and understandable pieces before we can process it.

#### Questions for Future Exploration

- Translation between infix and postfix notation.
- How do real calculators handle variable storage and retrieval?
- What other ways are there to create calculators? Do they all just use stacks and postfix evaluation? And push only values to the stack? How would it handle pushing things like `pi` and `e` to the stack?

#### What I'd Do Differently

- If possible, I'd like to think more of the end design and goal before implementation. Having to build things like variable storage and a last answer recall later was a bit tricky.

### Part 2: Virtual Machines

**Date Started**: 2025-10-05
**Date Completed**: 2025-10-11

#### Key Concepts Learned

- Fetch-decode-execute cycle
- Stack-based virtual machines
- Bytecode and instruction sets

#### Challenges Faced

- Initially understanding what bytecode is and how it relates to assembly and machine code.

#### Breakthrough Moments

- Realising bytecode execution is just reading instruction at current PC, do the thing, and then move PC forward (or jump).
- Understanding that a VM is a simple loop of fetch-decode-execute

#### Connections to Other Concepts

- Reuse of the stack calculator's stack for the VM's stack
- Arithmetic operations are similar to those in the stack calculator, but now as opcodes
- Prepares for next part on compilers, as we now have a target to compile to

#### Questions for Future Exploration

- How do real-world VMs like JVM and Python's VM work?
- What about register-based VMs?
- How can we optimize the VM? Or rather it's operations? Clearly takes forever to do a simple Fibonnaci or Factorial calculation right now.

#### What I'd Do Differently

- Refactor operations as they are mostly repeated code patterns.
- Build the disassembler before trying to build the demo programs, as it would've helped a lot in understanding and debugging the bytecode programs.

### Part 3: Simple Compiler (Design Phase)

**Date Started**: 2025-02-01
**Status**: Paused for Crafting Interpreters detour

#### Key Concepts Learned

- **Compilation pipeline**: source → tokens → AST → bytecode. Each stage transforms the representation.
- **Lexer vs Parser distinction**: Lexer produces flat token sequence (still "dumb" splitting). Parser is where structure emerges into AST.
- **Post-order traversal for codegen**: Process children before the node itself - same pattern as postfix evaluation. For `x = a + b`: generate code for `a + b` first (leaves result on stack), then emit STORE.
- **AST captures semantics, not syntax**: Left side of assignment is a *target* (STORE), right side usage of same variable is a *value* (LOAD). Same identifier, different meaning based on context.

#### Design Decisions Made

- **Brace-based syntax**: Simpler than indentation - no need for INDENT/DEDENT tokens
- **Simple operators only**: No `+=`, just `x = x + 1` - reduces lexer complexity
- **Integers only**: No floats for simplicity
- **No functions**: Would require CALL/RET and call stack in VM - significant extension

#### Bytecode Patterns Understood

**Assignment** (`x = expr`):
1. Generate code for expr (leaves value on stack)
2. Emit STORE x

**Binary operation** (`a + b`):
1. Generate code for left operand
2. Generate code for right operand  
3. Emit operator

**While loop**:
```
LOOP_START: <condition>
            JZ LOOP_END      ; exit if false
            <body>
            JMP LOOP_START
LOOP_END:   ...
```

#### Challenges Identified

- **Operator precedence**: `1 + 2 * 3` needs to parse as `1 + (2 * 3)`. Requires either layered recursive descent or Pratt parsing. More complex than initially expected.
- **Lookahead in lexer**: Need to peek ahead to distinguish `=` vs `==`, `<` vs `<=`
- **Jump address resolution**: When emitting JZ for a loop, don't know the target address yet. Need backpatching or two-pass approach.

#### Why Pausing for Crafting Interpreters

The design phase revealed that precedence parsing and error handling deserve proper treatment. Crafting Interpreters provides:
- Battle-tested implementation patterns
- Clear explanation of precedence parsing
- Complete working reference

Plan: Build Lox (or significant portions), then return with deeper understanding to complete this compiler.

#### Questions to Explore

- How does Pratt parsing work vs recursive descent with precedence levels?
- What design decisions does clox's VM make differently from mine?
- How do real compilers handle forward references (jumps to unknown addresses)?
- How should error recovery work - panic mode, synchronization points?

#### Connections to Other Concepts

- Post-order traversal for codegen mirrors postfix evaluation from Part 1
- Bytecode generation targets the VM from Part 2 - they're designed to work together
- Tokenization is similar to Part 1 but with lookahead for multi-character operators
- This rounds out the "how do computers execute programs" question from Phase 1

#### What I'd Do Differently

- Would have started with Crafting Interpreters as a reference from the beginning
- The mental model building was valuable, but implementation needs more structured guidance for something this complex

---

*Template for future entries:*

### Part X: [Topic]

**Date Started**:
**Date Completed**:

#### Key Concepts Learned

#### Challenges Faced

#### Breakthrough Moments

#### Connections to Other Concepts

#### Questions for Future Exploration

#### What I'd Do Differently

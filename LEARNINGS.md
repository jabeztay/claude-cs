# Learning Journal

## Phase 1: Computer Systems

### Part 1: Stack Calculator

**Date Started**: 2025-10-01
**Date Completed**: 2025-10-05

**Completed**
- Makefile for easy test running
- Stack data structure
- Tokenizer for calculator
  - Basic tokens: numbers, +, -, *, /
- Basic calculator evaluator
  - Handles simple expressions like "3 4 +"
  - Handles operators: +, -, *, /
- Calculator REPL

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

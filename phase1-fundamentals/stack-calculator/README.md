# Stack-Based Calculator

**Duration:** Week 1-2 (14 days)  
**Phase:** Computer Systems Fundamentals

## Learning Objectives
- Understand stack data structure in practice
- Learn about postfix notation and evaluation
- Grasp basic parsing concepts

## Project Goal
Build a calculator that evaluates expressions like `"3 4 + 2 *"` → `14`

## Implementation Steps
1. **Day 1-2:** Build basic stack operations (push, pop, peek)
2. **Day 3-4:** Implement postfix expression evaluator
3. **Day 5-7:** Add input parsing and error handling
4. **Day 8-10:** Extend with functions (sin, cos, sqrt)
5. **Day 11-14:** Add variables storage

## Code Structure
```
stack-calculator/
├── stack.py          # Stack implementation
├── tokenizer.py      # Break input into tokens
├── evaluator.py      # Core evaluation logic
├── main.py          # CLI interface
└── tests/           # Unit tests
```

## Deliverable
Calculator that evaluates postfix expressions with support for:
- Basic arithmetic operations (+, -, *, /)
- Mathematical functions (sin, cos, sqrt)
- Variable storage and retrieval
- Error handling for invalid expressions
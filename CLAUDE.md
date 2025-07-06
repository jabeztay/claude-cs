# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a "Claude Computer Science" curriculum repository - a project-based learning approach to computer science fundamentals. The curriculum is designed to teach CS concepts through building practical implementations rather than just theory.

## Development Commands

### Testing
```bash
# Run tests for the stack implementation
cd phase1-fundamentals/stack-calculator
python -m pytest tests/ -v

# Run specific test file
python -m pytest tests/test_stack.py -v

# Run all tests from project root
python -m pytest -v
```

### Python Environment
```bash
# The repository uses a virtual environment
source venv/bin/activate  # On Linux/Mac
# or
venv\Scripts\activate     # On Windows
```

## Architecture & Structure

### Phase-Based Learning Structure
The curriculum is organized into progressive phases:

1. **Phase 1: Computer Systems Fundamentals** (6-8 weeks)
   - Stack-based calculator → Virtual machine → Simple language compiler
   - Located in `phase1-fundamentals/`

2. **Phase 2: Data Structures in Action** (6-8 weeks)
   - Hash tables → Tree indexing → Persistent storage → Key-value store

3. **Phase 3: Database Internals** (8-10 weeks)
   - Storage engine → Query processing → Indexing → Transactions

4. **Phase 4: Distributed Systems** (8-10 weeks)
   - Network communication → Consensus algorithms → Fault tolerance

### Current Implementation Status
- **Phase 1 Stack Calculator**: Basic stack implementation with tests
  - `phase1-fundamentals/stack-calculator/stack.py`: Core stack data structure
  - `phase1-fundamentals/stack-calculator/tests/test_stack.py`: Test coverage using pytest
- **Phase 1 Calculator**: Basic calculator (placeholder)
  - `phase1-fundamentals/calculator/`: Calculator implementation directory

### Code Organization Principles
- Each phase builds on previous phases
- Projects are designed to be incrementally enhanced
- Focus on understanding through implementation rather than using existing libraries
- Test-driven development with pytest

## Development Guidelines

### Implementation Language
- Primary language: Python (for accessibility and rapid prototyping)
- Code should be educational and well-commented for learning purposes
- Type hints are used (as seen in `Stack` class)

### Testing Strategy
- Unit tests for all components using pytest
- Tests should be comprehensive and educational
- Test files follow `test_*.py` naming convention

### Project Structure Pattern
Each project follows this structure:
```
project-name/
├── core_module.py     # Main implementation
├── tests/            # Test directory
│   └── test_*.py    # Test files
└── main.py          # CLI interface (when applicable)
```

## Learning Resources Referenced
- "Crafting Interpreters" by Bob Nystrom
- "Database Internals" by Alex Petrov
- "Designing Data-Intensive Applications" by Martin Kleppmann
- MIT 6.824 Distributed Systems course
- CMU Database Systems Course (Andy Pavlo)
# Computer Science Fundamentals - Build to Learn Curriculum

**Duration:** 6-8 months total  
**Approach:** Project-based learning with theoretical backup  
**Goal:** Understand computer systems from first principles through building

---

## Phase 1: Computer Systems Fundamentals (6-8 weeks)
**Goal:** Understand how computers actually work

### Project: Build a Virtual Machine & Simple Language Interpreter

#### Week 1-2: Foundation - Stack-Based Calculator
**Learning Objectives:**
- Understand stack data structure in practice
- Learn about postfix notation and evaluation
- Grasp basic parsing concepts

**Deliverable:** Calculator that evaluates expressions like `"3 4 + 2 *"` → `14`

**Implementation Steps:**
1. **Day 1-2:** Build basic stack operations (push, pop, peek)
2. **Day 3-4:** Implement postfix expression evaluator
3. **Day 5-7:** Add input parsing and error handling
4. **Day 8-10:** Extend with functions (sin, cos, sqrt)
5. **Day 11-14:** Add variables storage

**Code Structure:**
```
calculator/
├── stack.py          # Stack implementation
├── tokenizer.py      # Break input into tokens
├── evaluator.py      # Core evaluation logic
├── main.py          # CLI interface
└── tests/           # Unit tests
```

#### Week 3-4: Simple Virtual Machine
**Learning Objectives:**
- Understand instruction sets and opcodes
- Learn about registers vs stack-based architectures
- Grasp memory organization

**Deliverable:** VM that executes bytecode instructions

**VM Design:**
```python
# Instruction Set
LOAD_CONST = 1    # Load constant onto stack
ADD = 2           # Pop two values, add, push result
SUB = 3           # Pop two values, subtract, push result
MUL = 4           # Pop two values, multiply, push result
STORE = 5         # Store top of stack to variable
LOAD_VAR = 6      # Load variable onto stack
PRINT = 7         # Print top of stack
HALT = 8          # Stop execution
```

#### Week 5-6: Simple Language Compiler
**Learning Objectives:**
- Understand compilation vs interpretation
- Learn lexical analysis and parsing
- Connect high-level syntax to low-level instructions

**Deliverable:** Compiler for a simple language that targets your VM

**Language Syntax:**
```javascript
// Your language should handle:
let x = 10 + 5;
let y = x * 2;
print(y);

if (x > 5) {
    print("x is big");
}
```

#### Week 7-8: Advanced Features & Optimization
**Enhancement Options (Pick 2-3):**
1. **Garbage Collection:** Simple mark-and-sweep
2. **Function Calls:** Call stack and local variables
3. **Debugging Features:** Step-through debugger
4. **Optimization:** Constant folding, dead code elimination
5. **Standard Library:** Built-in functions and modules

**Resources:**
- **"Crafting Interpreters"** by Bob Nystrom (free online)
- **Nand2Tetris** Chapters 1-5 (hardware), 7-12 (software)
- **CS Theory:** Computer organization, instruction sets, compilation

---

## Phase 2: Data Structures in Action (6-8 weeks)
**Goal:** Internalize algorithmic thinking through practical implementation

### Project: Build a Key-Value Store

#### Week 1-2: Hash Table Foundation
**Learning Objectives:**
- Understand hash functions and collision resolution
- Learn about load factors and performance characteristics
- Implement dynamic resizing

**Deliverable:** Hash table that handles insertions, lookups, deletions

**Implementation Features:**
- Multiple collision resolution strategies (chaining, open addressing)
- Dynamic resizing with rehashing
- Performance benchmarking tools

#### Week 3-4: Tree-Based Indexing
**Learning Objectives:**
- Understand balanced tree structures
- Learn about B-trees and their variants
- Grasp range queries and ordered iteration

**Deliverable:** B-tree implementation with range query support

#### Week 5-6: Persistent Storage
**Learning Objectives:**
- Understand file I/O and serialization
- Learn about write-ahead logging
- Grasp crash recovery mechanisms

**Deliverable:** Disk-based storage with durability guarantees

#### Week 7-8: Performance & Advanced Features
**Enhancement Options:**
- Bloom filters for faster negative lookups
- LRU cache implementation
- Compression and space optimization
- Concurrent access patterns

**Resources:**
- **CLRS** Chapters 11 (Hash Tables), 18 (B-Trees), 12-13 (BSTs)
- **"Database Internals"** by Alex Petrov (Chapters 1-7)
- **CS Theory:** Algorithm analysis, data structure trade-offs

---

## Phase 3: Database Internals (8-10 weeks)
**Goal:** Understand database design from first principles

### Project: Mini-Database Engine

#### Week 1-2: Storage Engine
**Learning Objectives:**
- Understand page-based storage
- Learn about buffer pool management
- Grasp ACID properties fundamentals

**Deliverable:** Basic storage engine with page management

#### Week 3-4: Query Processing
**Learning Objectives:**
- Understand SQL parsing and AST generation
- Learn about query planning and optimization
- Grasp different join algorithms

**Deliverable:** SQL subset parser and query executor

#### Week 5-6: Indexing System
**Learning Objectives:**
- Understand clustered vs non-clustered indexes
- Learn about index selection and maintenance
- Grasp multi-column and composite indexes

**Deliverable:** Index manager with B+ tree implementation

#### Week 7-8: Transaction Management
**Learning Objectives:**
- Understand isolation levels
- Learn about locking and deadlock detection
- Grasp two-phase commit

**Deliverable:** Transaction manager with concurrency control

#### Week 9-10: Advanced Features
**Enhancement Options:**
- Query optimization with statistics
- WAL-based recovery
- Basic replication
- Column-store vs row-store

**Resources:**
- **"Database System Concepts"** by Silberschatz (Chapters 10-16)
- **"Database Internals"** by Alex Petrov (Full book)
- **CMU Database Systems Course** (Andy Pavlo's lectures on YouTube)
- **CS Theory:** Database theory, query optimization, concurrency

---

## Phase 4: Distributed Systems (8-10 weeks)
**Goal:** Scale beyond single machines

### Project: Distributed Key-Value Store

#### Week 1-2: Network Communication
**Learning Objectives:**
- Understand RPC and message passing
- Learn about serialization protocols
- Grasp network partitions and timeouts

**Deliverable:** Basic distributed KV store with network communication

#### Week 3-4: Consensus Algorithm
**Learning Objectives:**
- Understand the Raft consensus algorithm
- Learn about leader election and log replication
- Grasp split-brain scenarios

**Deliverable:** Raft implementation with leader election

#### Week 5-6: Fault Tolerance
**Learning Objectives:**
- Understand CAP theorem in practice
- Learn about failure detection
- Grasp data consistency models

**Deliverable:** Fault-tolerant cluster with automated failover

#### Week 7-8: Scaling & Performance
**Learning Objectives:**
- Understand partitioning strategies
- Learn about load balancing
- Grasp eventual consistency

**Deliverable:** Horizontally scalable distributed system

#### Week 9-10: Advanced Topics
**Enhancement Options:**
- Byzantine fault tolerance
- Gossip protocols
- Vector clocks
- Distributed transactions

**Resources:**
- **"Designing Data-Intensive Applications"** by Martin Kleppmann
- **MIT 6.824** Distributed Systems course materials
- **"Distributed Systems"** by Tanenbaum and Van Steen
- **Papers:** Raft paper, Google MapReduce, Amazon Dynamo
- **CS Theory:** Consensus algorithms, distributed consistency, fault tolerance

---

## Learning Strategy & Tips

### Weekly Structure
- **Monday-Wednesday:** Core implementation work
- **Thursday:** CS theory deep-dive and reading
- **Friday:** Testing, documentation, and reflection
- **Weekend:** Optional extensions or catch-up

### Assessment Milestones
- **End of each phase:** Working demo and code review
- **Mid-phase:** Technical blog post explaining key concepts
- **Project completion:** GitHub repo with comprehensive README

### Recommended Tools
- **Language:** Python (easier) or Go/Rust (more systems-like)
- **Testing:** Unit tests for all components
- **Documentation:** Clear README with examples
- **Version Control:** Git with meaningful commit messages

### Success Metrics
By completion, you should be able to:
1. **Explain** fundamental computer science concepts from first principles
2. **Implement** basic versions of complex systems
3. **Debug** performance and correctness issues
4. **Design** scalable solutions with understanding of trade-offs
5. **Contribute** meaningfully to technical discussions

---

## Alternative Resources by Topic

### Computer Architecture
- **Nand2Tetris** (Comprehensive, project-based)
- **Computer Systems: A Programmer's Perspective** (CSAPP)
- **"Code" by Charles Petzold** (Accessible introduction)

### Algorithms & Data Structures
- **CLRS** (Comprehensive reference)
- **Algorithm Design Manual** by Skiena (Practical focus)
- **Algorithms** by Sedgewick (Visual and intuitive)

### Database Systems
- **"Transaction Processing" by Gray and Reuter** (Advanced)
- **"Readings in Database Systems" (Red Book)** (Papers collection)
- **PostgreSQL source code** (Real-world implementation study)

### Distributed Systems
- **"Distributed Algorithms" by Lynch** (Theoretical foundation)
- **Google Research Papers** (MapReduce, Bigtable, Spanner)
- **Jepsen blog** (Real-world distributed systems testing)

---

## Getting Started

1. **Choose your implementation language** (Python recommended for beginners)
2. **Set up development environment** with testing framework
3. **Create project repository** structure
4. **Begin Phase 1, Week 1** with the stack calculator
5. **Join communities:** relevant Discord/Slack channels, Reddit communities
6. **Document your journey:** Blog posts, GitHub updates, learning reflections

**Remember:** The goal is deep understanding through building, not just completing projects. Take time to understand the "why" behind each design decision.

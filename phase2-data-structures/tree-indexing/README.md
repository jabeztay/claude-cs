# Tree-Based Indexing

**Duration:** Week 3-4 (14 days)  
**Phase:** Data Structures in Action

## Learning Objectives
- Understand balanced tree structures
- Learn about B-trees and their variants
- Grasp range queries and ordered iteration

## Project Goal
Build a B-tree implementation with range query support

## Implementation Features
- Self-balancing B-tree structure
- Range query capabilities
- Ordered iteration support
- Node splitting and merging

## Code Structure
```
tree-indexing/
├── btree.py           # B-tree implementation
├── btree_node.py      # Node structure and operations
├── range_query.py     # Range query implementation
├── iterator.py        # Ordered iteration
├── main.py           # Demo and CLI
└── tests/            # Unit tests
```

## Key Components
1. **B-tree Structure:** Self-balancing tree with configurable order
2. **Node Operations:** Insert, delete, search, split, merge
3. **Range Queries:** Efficient range-based lookups
4. **Ordered Iteration:** In-order traversal support

## B-tree Properties
- Configurable order (minimum degree)
- All leaves at same level
- Internal nodes have multiple keys
- Efficient for disk-based storage

## Deliverable
B-tree implementation with:
- O(log n) insertion, deletion, search
- Range query support
- Ordered iteration capabilities
- Comprehensive test coverage

## Performance Targets
- Balanced tree maintenance
- Efficient range queries
- Minimal tree height
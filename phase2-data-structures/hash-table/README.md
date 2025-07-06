# Hash Table Foundation

**Duration:** Week 1-2 (14 days)  
**Phase:** Data Structures in Action

## Learning Objectives
- Understand hash functions and collision resolution
- Learn about load factors and performance characteristics
- Implement dynamic resizing

## Project Goal
Build a hash table that handles insertions, lookups, and deletions

## Implementation Features
- Multiple collision resolution strategies (chaining, open addressing)
- Dynamic resizing with rehashing
- Performance benchmarking tools

## Code Structure
```
hash-table/
├── hash_table.py       # Main hash table implementation
├── hash_functions.py   # Different hash function implementations
├── collision_resolution.py # Chaining and open addressing
├── benchmarks.py       # Performance testing
├── main.py            # Demo and CLI
└── tests/             # Unit tests
```

## Key Components
1. **Hash Functions:** Implement multiple hash functions (djb2, FNV, etc.)
2. **Collision Resolution:** Both chaining and open addressing
3. **Dynamic Resizing:** Automatic table growth/shrink
4. **Performance Metrics:** Load factor monitoring, collision statistics

## Deliverable
Hash table implementation with:
- O(1) average case insertion, lookup, deletion
- Configurable collision resolution strategies
- Dynamic resizing based on load factor
- Comprehensive performance benchmarks

## Performance Targets
- Load factor maintenance (0.75 threshold)
- Minimal collision chains
- Efficient rehashing on resize
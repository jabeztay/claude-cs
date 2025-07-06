# Persistent Storage

**Duration:** Week 5-6 (14 days)  
**Phase:** Data Structures in Action

## Learning Objectives
- Understand file I/O and serialization
- Learn about write-ahead logging
- Grasp crash recovery mechanisms

## Project Goal
Build disk-based storage with durability guarantees

## Implementation Features
- File-based data persistence
- Write-ahead logging (WAL)
- Crash recovery mechanisms
- Serialization/deserialization

## Code Structure
```
persistent-storage/
├── storage_engine.py  # Main storage interface
├── file_manager.py    # File I/O operations
├── wal.py            # Write-ahead logging
├── serializer.py     # Data serialization
├── recovery.py       # Crash recovery
├── main.py           # Demo and CLI
└── tests/            # Unit tests
```

## Key Components
1. **Storage Engine:** Main interface for persistent operations
2. **File Manager:** Low-level file I/O and page management
3. **WAL System:** Write-ahead logging for durability
4. **Recovery:** Crash recovery and consistency checking

## Durability Features
- ACID compliance (Atomicity, Consistency, Isolation, Durability)
- Transaction log management
- Checkpoint mechanisms
- Data integrity verification

## Deliverable
Persistent storage system with:
- Durable data storage on disk
- Write-ahead logging implementation
- Crash recovery capabilities
- Transaction-safe operations

## Performance Targets
- Efficient disk I/O
- Minimal recovery time
- Data integrity guarantees
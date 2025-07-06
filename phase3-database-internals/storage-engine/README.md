# Storage Engine

**Duration:** Week 1-2 (14 days)  
**Phase:** Database Internals

## Learning Objectives
- Understand page-based storage
- Learn about buffer pool management
- Grasp ACID properties fundamentals

## Project Goal
Build a basic storage engine with page management

## Implementation Features
- Page-based storage architecture
- Buffer pool management
- Basic ACID property support
- Disk page allocation and deallocation

## Code Structure
```
storage-engine/
├── storage_engine.py  # Main storage engine
├── page_manager.py    # Page allocation/deallocation
├── buffer_pool.py     # Buffer pool management
├── disk_manager.py    # Disk I/O operations
├── page.py           # Page structure and operations
├── main.py           # Demo and CLI
└── tests/            # Unit tests
```

## Key Components
1. **Storage Engine:** Main interface for storage operations
2. **Page Manager:** Handle page allocation and organization
3. **Buffer Pool:** In-memory cache for frequently accessed pages
4. **Disk Manager:** Low-level disk I/O operations

## Storage Features
- Fixed-size page architecture
- Page replacement policies (LRU)
- Write-through/write-back caching
- Page pinning mechanisms

## Deliverable
Storage engine with:
- Page-based storage management
- Buffer pool with LRU replacement
- Basic durability guarantees
- Efficient disk I/O handling

## Performance Targets
- Efficient page caching
- Minimal disk I/O
- Fast page allocation/deallocation
PHASE1_PART1 = phase1-computer-systems/part1-stack-calculator
PHASE1_PART2 = phase1-computer-systems/part2-virtual-machine

.PHONY: help test clean

help:
	@echo "Available commands:"
	@echo "  make test-1-1      - Run phase 1 part 1 tests"
	@echo "  make test-all      - Run all tests"
	@echo "  make coverage-1-1  - Coverage for phase 1 part 1"
	@echo "  make coverage-all  - Run all coverage"
	@echo "  make clean         - Clean all artifacts"

clean:
	@echo "Cleaning up..."
	find . -type d -name '__pycache__' -exec rm -rf {} +
	find . -type d -name '.pytest_cache' -exec rm -rf {} +
	find . -type f -name '.coverage' -delete

test-all:
	@echo "Running all tests..."
	$(MAKE) test-1-1
	$(MAKE) test-1-2

coverage-all:
	@echo "Running all coverage..."
	$(MAKE) coverage-1-1
	$(MAKE) coverage-1-2

test-1-1:
	@echo "Running tests for Phase 1 Part 1..."
	cd ./$(PHASE1_PART1) && PYTHONPATH=src pytest tests/ -v

coverage-1-1:
	@echo "Running coverage tests for Phase 1 Part 1..."
	cd ./$(PHASE1_PART1) && PYTHONPATH=src pytest tests/ -v --cov=src --cov-report=term-missing tests/

test-1-2:
	@echo "Running tests for Phase 1 Part 2..."
	cd ./$(PHASE1_PART2) && PYTHONPATH=src pytest tests/ -v

coverage-1-2:
	@echo "Running coverage tests for Phase 1 Part 2..."
	cd ./$(PHASE1_PART2) && PYTHONPATH=src pytest tests/ -v --cov=src --cov-report=term-missing tests/

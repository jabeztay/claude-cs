from typing import Any


LOAD_CONST = 1    # Load constant onto stack
ADD = 2           # Pop two values, add, push result
SUB = 3           # Pop two values, subtract, push result
MUL = 4           # Pop two values, multiply, push result
STORE = 5         # Store top of stack to variable
LOAD_VAR = 6      # Load variable onto stack
PRINT = 7         # Print top of stack
HALT = 8          # Stop execution


class Stack:
    def __init__(self):
        self._stack = []

    def __len__(self):
        return len(self._stack)

    def push(self, value: Any):
        self._stack.append(value)

    def pop(self):
        if self._stack:
            return self._stack.pop()
        return None

    def peek(self):
        if self._stack:
            return self._stack[-1]
        return None


class VirtualMachine:
    def __init__(self):
        self.pc = 0
        self.bytecode = []
        self.stack = Stack()
        self.variables = {}
        self.running = False

        self.dispatch = {
            LOAD_CONST: self.execute_load_const,
            HALT: self.execute_halt,
            ADD: self.execute_add,
            PRINT: self.execute_print,
            MUL: self.execute_mul,
            SUB: self.execute_sub,
            STORE: self.execute_store,
            LOAD_VAR: self.execute_load_var,
        }

    def run(self, bytecode: list[int]) -> None:
        self.bytecode = bytecode
        self.pc = 0
        self.running = True

        while self.running and self.pc < len(bytecode):
            instruction = self.bytecode[self.pc]

            if instruction in self.dispatch:
                operation = self.dispatch[instruction]
                operation()

            else:
                self.running = False

            self.pc += 1

    def execute_load_const(self):
        self.pc += 1
        self.stack.push(self.bytecode[self.pc])

    def execute_halt(self):
        self.running = False

    def execute_add(self):
        a, b = self.stack.pop(), self.stack.pop()
        self.stack.push(a + b)

    def execute_print(self):
        print(self.stack.peek())

    def execute_mul(self):
        a, b = self.stack.pop(), self.stack.pop()
        self.stack.push(a * b)

    def execute_sub(self):
        a, b = self.stack.pop(), self.stack.pop()
        self.stack.push(b - a)

    def execute_store(self):
        self.pc += 1
        var_name = self.bytecode[self.pc]
        self.variables[var_name] = self.stack.pop()

    def execute_load_var(self):
        self.pc += 1
        var_name = self.bytecode[self.pc]
        var_value = self.variables[var_name]
        self.stack.push(var_value)

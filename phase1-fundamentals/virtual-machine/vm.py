from typing import Any


LOAD_CONST = 1         # Load constant onto stack
ADD = 2                # Pop two values, add, push result
SUB = 3                # Pop two values, subtract, push result
MUL = 4                # Pop two values, multiply, push result
STORE = 5              # Store top of stack to variable
LOAD_VAR = 6           # Load variable onto stack
PRINT = 7              # Print top of stack
HALT = 8               # Stop execution
JUMP = 9               # Jump to address
JUMP_IF_ZERO = 10      # Jump to address if top of stack is 0
JUMP_IF_NOT_ZERO = 11  # Jump to address if top of stack is not 0
GT = 12                # Pop b, pop a, push 1 if a > b else 0
LT = 13                # Pop b, pop a, push 1 if a < b else 0
EQ = 14                # Pop b, pop a, push 1 if a == b else 0
GEQ = 15               # Pop b, pop a, push 1 if a >= b else 0
LEQ = 16               # Pop b, pop a, push 1 if a <= b else 0
DIV = 17               # Pop two values, divide, push result


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
            JUMP: self.execute_jump,
            JUMP_IF_NOT_ZERO: self.execute_jump_if_not_zero,
            JUMP_IF_ZERO: self.execute_jump_if_zero,
            GT: self.execute_gt,
            LT: self.execute_lt,
            EQ: self.execute_eq,
            GEQ: self.execute_geq,
            LEQ: self.execute_leq,
            DIV: self.execute_div,
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
        b, a = self.stack.pop(), self.stack.pop()
        self.stack.push(a + b)

    def execute_print(self):
        print(self.stack.pop())

    def execute_mul(self):
        b, a = self.stack.pop(), self.stack.pop()
        self.stack.push(a * b)

    def execute_sub(self):
        b, a = self.stack.pop(), self.stack.pop()
        self.stack.push(a - b)

    def execute_store(self):
        self.pc += 1
        var_name = self.bytecode[self.pc]
        self.variables[var_name] = self.stack.pop()

    def execute_load_var(self):
        self.pc += 1
        var_name = self.bytecode[self.pc]
        var_value = self.variables[var_name]
        self.stack.push(var_value)

    def execute_gt(self):
        b, a = self.stack.pop(), self.stack.pop()
        result = 1 if a > b else 0
        self.stack.push(result)

    def execute_lt(self):
        b, a = self.stack.pop(), self.stack.pop()
        result = 1 if a < b else 0
        self.stack.push(result)

    def execute_eq(self):
        b, a = self.stack.pop(), self.stack.pop()
        result = 1 if a == b else 0
        self.stack.push(result)

    def execute_geq(self):
        b, a = self.stack.pop(), self.stack.pop()
        result = 1 if a >= b else 0
        self.stack.push(result)

    def execute_leq(self):
        b, a = self.stack.pop(), self.stack.pop()
        result = 1 if a <= b else 0
        self.stack.push(result)

    def execute_jump(self):
        self.pc += 1
        new_address = self.bytecode[self.pc]
        self.pc = new_address - 1

    def execute_jump_if_not_zero(self):
        a = self.stack.pop()
        self.pc += 1
        if a != 0:
            new_address = self.bytecode[self.pc]
            self.pc = new_address - 1

    def execute_jump_if_zero(self):
        a = self.stack.pop()
        self.pc += 1
        if a == 0:
            new_address = self.bytecode[self.pc]
            self.pc = new_address - 1

    def execute_div(self):
        b, a = self.stack.pop(), self.stack.pop()
        self.stack.push(a / b)

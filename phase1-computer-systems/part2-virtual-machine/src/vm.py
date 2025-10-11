from opcodes import Opcode
from stack import Stack


class VirtualMachineError(Exception):
    """Raised for errors in the virtual machine."""

    pass


class VirtualMachine:
    def __init__(self, memory_size=256) -> None:
        self._stack = Stack()
        self._memory = [0] * memory_size
        self._pc = 0

    def run(self, bytecode: list[int]) -> None:
        """Run the provided bytecode."""
        while True:
            try:
                opcode = Opcode(bytecode[self._pc])
            except ValueError:
                raise VirtualMachineError(
                    f"Invalid opcode at pc {self._pc}: {bytecode[self._pc]}"
                )

            match opcode:
                case Opcode.HALT:
                    break
                case Opcode.PUSH:
                    self._push(bytecode)
                case Opcode.PRINT:
                    self._print()
                case Opcode.ADD:
                    self._add()
                case Opcode.SUB:
                    self._sub()
                case Opcode.MUL:
                    self._mul()
                case Opcode.DIV:
                    self._div()
                case Opcode.GT:
                    self._gt()
                case Opcode.LT:
                    self._lt()
                case Opcode.EQ:
                    self._eq()
                case Opcode.GE:
                    self._ge()
                case Opcode.LE:
                    self._le()
                case Opcode.NEQ:
                    self._neq()
                case Opcode.JMP:
                    self._jmp(bytecode)
                case Opcode.JZ:
                    self._jz(bytecode)
                case Opcode.JNZ:
                    self._jnz(bytecode)
                case Opcode.DUP:
                    self._dup()
                case Opcode.SWAP:
                    self._swap()
                case Opcode.POP:
                    self._pop()
                case Opcode.STORE:
                    self._store(bytecode)
                case Opcode.LOAD:
                    self._load(bytecode)
                case _:
                    raise NotImplementedError(f"Opcode not implemented: {opcode}")

    def _load(self, bytecode: list[int]) -> None:
        """Load a value from memory at specified location onto the stack."""
        self._pc += 1
        address = bytecode[self._pc]
        if not (0 <= address < len(self._memory)):
            raise VirtualMachineError(f"Invalid memory address: {address}")
        value = self._memory[address]
        self._stack.push(value)
        self._pc += 1

    def _store(self, bytecode: list[int]) -> None:
        """Store the top value from the stack into memory at specified location."""
        self._pc += 1
        address = bytecode[self._pc]
        value = self._stack.pop()
        if not (0 <= address < len(self._memory)):
            raise VirtualMachineError(f"Invalid memory address: {address}")
        self._memory[address] = value
        self._pc += 1

    def _pop(self) -> None:
        """Pop the top value from the stack."""
        self._stack.pop()
        self._pc += 1

    def _swap(self) -> None:
        """Swap the top two values on the stack."""
        first = self._stack.pop()
        second = self._stack.pop()
        self._stack.push(first)
        self._stack.push(second)
        self._pc += 1

    def _dup(self) -> None:
        """Duplicate the top value on the stack."""
        value = self._stack.peek()
        self._stack.push(value)
        self._pc += 1

    def _print(self) -> None:
        value = self._stack.pop()
        print(value)
        self._pc += 1

    def _push(self, bytecode) -> None:
        """Push a value onto the stack."""
        self._pc += 1
        value = bytecode[self._pc]
        self._stack.push(value)
        self._pc += 1

    def _add(self) -> None:
        """Pop two values from the stack, add them, and push the result."""
        right = self._stack.pop()
        left = self._stack.pop()
        self._stack.push(left + right)
        self._pc += 1

    def _sub(self) -> None:
        """Pop two values from the stack, subtract them, and push the result."""
        right = self._stack.pop()
        left = self._stack.pop()
        self._stack.push(left - right)
        self._pc += 1

    def _mul(self) -> None:
        """Pop two values from the stack, multiply them, and push the result."""
        right = self._stack.pop()
        left = self._stack.pop()
        self._stack.push(left * right)
        self._pc += 1

    def _div(self) -> None:
        """Pop two values from the stack, divide them, and push the result."""
        right = self._stack.pop()
        left = self._stack.pop()
        self._stack.push(left // right)
        self._pc += 1

    def _gt(self) -> None:
        """Pop two values from the stack, compare them, and push the result."""
        right = self._stack.pop()
        left = self._stack.pop()
        self._stack.push(1 if left > right else 0)
        self._pc += 1

    def _lt(self) -> None:
        """Pop two values from the stack, compare them, and push the result."""
        right = self._stack.pop()
        left = self._stack.pop()
        self._stack.push(1 if left < right else 0)
        self._pc += 1

    def _eq(self) -> None:
        """Pop two values from the stack, compare them, and push the result."""
        right = self._stack.pop()
        left = self._stack.pop()
        self._stack.push(1 if left == right else 0)
        self._pc += 1

    def _ge(self) -> None:
        """Pop two values from the stack, compare them, and push the result."""
        right = self._stack.pop()
        left = self._stack.pop()
        self._stack.push(1 if left >= right else 0)
        self._pc += 1

    def _le(self) -> None:
        """Pop two values from the stack, compare them, and push the result."""
        right = self._stack.pop()
        left = self._stack.pop()
        self._stack.push(1 if left <= right else 0)
        self._pc += 1

    def _neq(self) -> None:
        """Pop two values from the stack, compare them, and push the result."""
        right = self._stack.pop()
        left = self._stack.pop()
        self._stack.push(1 if left != right else 0)
        self._pc += 1

    def _jmp(self, bytecode) -> None:
        """Jump to the specified address."""
        self._pc += 1
        address = bytecode[self._pc]
        self._pc = address

    def _jz(self, bytecode) -> None:
        """Pop a value from the stack and jump if it's zero."""
        value = self._stack.pop()
        self._pc += 1
        address = bytecode[self._pc]
        if value == 0:
            self._pc = address
        else:
            self._pc += 1

    def _jnz(self, bytecode) -> None:
        """Pop a value from the stack and jump if it's not zero."""
        value = self._stack.pop()
        self._pc += 1
        address = bytecode[self._pc]
        if value != 0:
            self._pc = address
        else:
            self._pc += 1

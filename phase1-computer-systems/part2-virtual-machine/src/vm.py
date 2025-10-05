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
                case _:
                    raise NotImplementedError(f"Opcode not implemented: {opcode}")

    def _print(self):
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

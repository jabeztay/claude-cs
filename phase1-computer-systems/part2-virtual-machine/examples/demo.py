import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from opcodes import Opcode
from vm import VirtualMachine


def factorial(n: int) -> list[int]:
    """Generate bytecode to compute factorial of n."""
    return [
        Opcode.PUSH.value,
        n,
        Opcode.STORE.value,
        0,
        Opcode.PUSH.value,
        1,
        Opcode.STORE.value,
        1,
        Opcode.LOAD.value,
        0,
        Opcode.LOAD.value,
        1,
        Opcode.MUL.value,
        Opcode.STORE.value,
        1,
        Opcode.LOAD.value,
        0,
        Opcode.PUSH.value,
        1,
        Opcode.SUB.value,
        Opcode.DUP.value,
        Opcode.STORE.value,
        0,
        Opcode.PUSH.value,
        1,
        Opcode.GE.value,
        Opcode.JNZ.value,
        8,
        Opcode.LOAD.value,
        1,
        Opcode.PRINT.value,
        Opcode.HALT.value,
    ]


def fibonacci(n: int) -> list[int]:
    """Generate bytecode to print first n Fibonacci numbers."""
    return [
        Opcode.PUSH.value,
        0,
        Opcode.STORE.value,
        0,
        Opcode.PUSH.value,
        1,
        Opcode.STORE.value,
        1,
        Opcode.PUSH.value,
        n,
        Opcode.STORE.value,
        2,
        Opcode.LOAD.value,
        0,
        Opcode.DUP.value,
        Opcode.PRINT.value,
        Opcode.LOAD.value,
        1,
        Opcode.ADD.value,
        Opcode.LOAD.value,
        1,
        Opcode.STORE.value,
        0,
        Opcode.STORE.value,
        1,
        Opcode.LOAD.value,
        2,
        Opcode.PUSH.value,
        1,
        Opcode.SUB.value,
        Opcode.DUP.value,
        Opcode.STORE.value,
        2,
        Opcode.PUSH.value,
        1,
        Opcode.GE.value,
        Opcode.JNZ.value,
        12,
        Opcode.HALT.value,
    ]


if __name__ == "__main__":
    vm = VirtualMachine()
    bytecode = factorial(5)
    vm.run(bytecode)  # 120

    vm = VirtualMachine()
    bytecode = fibonacci(10)
    vm.run(bytecode)  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

    from disassembler import disassemble

    print("\nDisassembly of factorial(5):")
    print(disassemble(factorial(5)))
    print("\nDisassembly of fibonacci(10):")
    print(disassemble(fibonacci(10)))

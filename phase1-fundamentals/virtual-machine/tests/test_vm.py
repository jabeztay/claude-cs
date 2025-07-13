import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from vm import *


def test_calculations():
    vm = VirtualMachine()
    bytecode = [
        LOAD_CONST, 10,
        LOAD_CONST, 5,
        ADD,
        LOAD_CONST, 3,
        MUL,
        LOAD_CONST, 2,
        SUB,
        HALT
    ]
    vm.run(bytecode)

    assert vm.stack.peek() == 43


    bytecode = [
        LOAD_CONST, 42,
        STORE, "x",
        LOAD_VAR, "x",
        HALT
    ]
    vm.run(bytecode)

    assert vm.stack.peek() == 42

    bytecode = [
        LOAD_CONST, 5,
        LOAD_CONST, 3,
        GT,
        HALT
    ]
    vm.run(bytecode)

    assert vm.stack.peek() == 1

    bytecode = [
        LOAD_CONST, 5,
        LOAD_CONST, 3,
        GT,
        JUMP_IF_NOT_ZERO, 10,
        LOAD_CONST, "small", HALT,
        LOAD_CONST, "big", HALT,
    ]
    vm.run(bytecode)

    """
    counter = 1
    while counter <= 3:
        print(counter)
        counter = counter + 1
   """

    assert vm.stack.peek() == "big"

    bytecode = [
        LOAD_CONST, 1,
        STORE, "counter",
        LOAD_VAR, "counter",
        LOAD_CONST, 3,
        LEQ,
        JUMP_IF_ZERO, 22,
        LOAD_VAR, "counter",
        PRINT,
        LOAD_VAR, "counter",
        LOAD_CONST, 1,
        ADD,
        STORE, "counter",
        JUMP, 4,
        HALT,
    ]
    vm.run(bytecode)
    bytecode = [
        LOAD_VAR, "counter"
    ]
    vm.run(bytecode)
    assert vm.stack.peek() == 4

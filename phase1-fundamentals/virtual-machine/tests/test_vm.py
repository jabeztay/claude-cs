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
        PRINT,
        HALT
    ]
    vm.run(bytecode)

    assert vm.stack.peek() == 43


    bytecode = [
        LOAD_CONST, 42,
        STORE, "x",
        LOAD_VAR, "x",
        PRINT,
        HALT
    ]
    vm.run(bytecode)

    assert vm.stack.peek() == 42

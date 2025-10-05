from enum import Enum


class Opcode(Enum):
    HALT = 0
    LOAD = 1
    STORE = 2
    PUSH = 3
    POP = 4
    DUP = 5
    SWAP = 6
    ADD = 7
    SUB = 8
    MUL = 9
    DIV = 10
    EQ = 11
    NEQ = 12
    LT = 13
    GT = 14
    LE = 15
    GE = 16
    JMP = 17
    JZ = 18
    JNZ = 19
    PRINT = 20

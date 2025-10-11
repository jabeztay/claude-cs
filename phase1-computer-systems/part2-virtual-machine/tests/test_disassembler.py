from disassembler import disassemble
from opcodes import Opcode


def test_disassemble_no_operands():
    """Test disassemble with no operands."""
    bytecode = [
        Opcode.ADD.value,
        Opcode.PRINT.value,
        Opcode.HALT.value,
    ]
    result = disassemble(bytecode)
    expected = "0000: ADD\n" "0001: PRINT\n" "0002: HALT\n"
    assert result == expected


def test_disassemble_with_operands():
    """Test disassemble with operands."""
    bytecode = [
        Opcode.PUSH.value,
        42,
        Opcode.PRINT.value,
        Opcode.HALT.value,
    ]
    disassembled = disassemble(bytecode)
    expected = "0000: PUSH 42\n" "0002: PRINT\n" "0003: HALT\n"
    assert disassembled == expected


def test_disassemble_with_jumps():
    """Test disassemble with jump instructions."""
    bytecode = [
        Opcode.JMP.value,
        5,
        Opcode.PUSH.value,
        0,
        Opcode.PRINT.value,
        Opcode.HALT.value,
    ]
    disassembled = disassemble(bytecode)
    expected = "0000: JMP 5\n" "0002: PUSH 0\n" "0004: PRINT\n" "0005: HALT\n"
    assert disassembled == expected

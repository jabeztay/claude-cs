from opcodes import Opcode

OPCODES_WITH_OPERANDS = {
    Opcode.PUSH,
    Opcode.LOAD,
    Opcode.STORE,
    Opcode.JMP,
    Opcode.JZ,
    Opcode.JNZ,
}


def disassemble(bytecode: list[int]) -> str:
    """Disassemble bytecode to human-readable format."""
    output = []
    pc = 0

    while pc < len(bytecode):
        operation = bytecode[pc]
        try:
            opcode = Opcode(operation)
            if opcode in OPCODES_WITH_OPERANDS:
                pc += 1
                if pc < len(bytecode):
                    operand = bytecode[pc]
                    output.append(f"{pc-1:04}: {opcode.name} {operand}")
                else:
                    output.append(f"{pc-1:04}: {opcode.name} <missing operand>")
            else:
                output.append(f"{pc:04}: {opcode.name}")
            pc += 1
        except ValueError:
            output.append(f"{pc:04}: UNKNOWN_OPCODE {operation}")
            pc += 1
            continue

    return "\n".join(output) + "\n"

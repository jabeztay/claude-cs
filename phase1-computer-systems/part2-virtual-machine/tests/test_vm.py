import pytest
from opcodes import Opcode
from vm import VirtualMachine, VirtualMachineError


@pytest.fixture
def vm():
    return VirtualMachine()


def test_vm_initialization(vm):
    """Test VM initialization."""
    assert vm._pc == 0
    assert len(vm._memory) == 256
    assert vm._stack.is_empty()


def test_vm_basic_bytecode(vm, capsys):
    """Test VM with basic bytecode."""
    bytecode = [Opcode.PUSH.value, 42, Opcode.PRINT.value, Opcode.HALT.value]
    vm.run(bytecode)
    captured = capsys.readouterr()
    assert captured.out == "42\n"


def test_vm_add_bytecode(vm, capsys):
    """Test VM with addition bytecode."""
    bytecode = [
        Opcode.PUSH.value,
        21,
        Opcode.PUSH.value,
        21,
        Opcode.ADD.value,
        Opcode.PRINT.value,
        Opcode.HALT.value,
    ]
    vm.run(bytecode)
    captured = capsys.readouterr()
    assert captured.out == "42\n"


def test_vm_sub_bytecode(vm, capsys):
    """Test VM with subtraction bytecode."""
    bytecode = [
        Opcode.PUSH.value,
        50,
        Opcode.PUSH.value,
        8,
        Opcode.SUB.value,
        Opcode.PRINT.value,
        Opcode.HALT.value,
    ]
    vm.run(bytecode)
    captured = capsys.readouterr()
    assert captured.out == "42\n"


def test_vm_mul_bytecode(vm, capsys):
    """Test VM with multiplication bytecode."""
    bytecode = [
        Opcode.PUSH.value,
        6,
        Opcode.PUSH.value,
        7,
        Opcode.MUL.value,
        Opcode.PRINT.value,
        Opcode.HALT.value,
    ]
    vm.run(bytecode)
    captured = capsys.readouterr()
    assert captured.out == "42\n"


def test_vm_div_bytecode(vm, capsys):
    """Test VM with division bytecode."""
    bytecode = [
        Opcode.PUSH.value,
        84,
        Opcode.PUSH.value,
        2,
        Opcode.DIV.value,
        Opcode.PRINT.value,
        Opcode.HALT.value,
    ]
    vm.run(bytecode)
    captured = capsys.readouterr()
    assert captured.out == "42\n"


def test_vm_unknown_opcode(vm):
    """Test VM with unknown opcode."""
    bytecode = [99, Opcode.HALT.value]
    with pytest.raises(VirtualMachineError):
        vm.run(bytecode)

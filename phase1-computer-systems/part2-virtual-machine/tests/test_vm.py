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


@pytest.mark.parametrize(
    "left,right,expected", [(5, 3, "1\n"), (3, 5, "0\n"), (3, 3, "0\n")]
)
def test_vm_gt_true(left, right, expected, vm, capsys):
    """Test VM with greater-than comparison bytecode."""
    bytecode = [
        Opcode.PUSH.value,
        left,
        Opcode.PUSH.value,
        right,
        Opcode.GT.value,
        Opcode.PRINT.value,
        Opcode.HALT.value,
    ]
    vm.run(bytecode)
    captured = capsys.readouterr()
    assert captured.out == expected


@pytest.mark.parametrize(
    "left,right,expected", [(2, 3, "1\n"), (3, 2, "0\n"), (3, 3, "0\n")]
)
def test_vm_lt(left, right, expected, vm, capsys):
    """Test VM with less-than comparison bytecode."""
    bytecode = [
        Opcode.PUSH.value,
        left,
        Opcode.PUSH.value,
        right,
        Opcode.LT.value,
        Opcode.PRINT.value,
        Opcode.HALT.value,
    ]
    vm.run(bytecode)
    captured = capsys.readouterr()
    assert captured.out == expected


@pytest.mark.parametrize(
    "left,right,expected", [(3, 3, "1\n"), (3, 4, "0\n"), (4, 3, "0\n")]
)
def test_vm_eq(left, right, expected, vm, capsys):
    """Test VM with equality comparison bytecode."""
    bytecode = [
        Opcode.PUSH.value,
        left,
        Opcode.PUSH.value,
        right,
        Opcode.EQ.value,
        Opcode.PRINT.value,
        Opcode.HALT.value,
    ]
    vm.run(bytecode)
    captured = capsys.readouterr()
    assert captured.out == expected


@pytest.mark.parametrize(
    "left,right,expected", [(3, 3, "1\n"), (2, 3, "0\n"), (4, 3, "1\n")]
)
def test_vm_ge(left, right, expected, vm, capsys):
    """Test VM with greater-than-or-equal comparison bytecode."""
    bytecode = [
        Opcode.PUSH.value,
        left,
        Opcode.PUSH.value,
        right,
        Opcode.GE.value,
        Opcode.PRINT.value,
        Opcode.HALT.value,
    ]
    vm.run(bytecode)
    captured = capsys.readouterr()
    assert captured.out == expected


@pytest.mark.parametrize(
    "left,right,expected", [(3, 3, "1\n"), (2, 3, "1\n"), (4, 3, "0\n")]
)
def test_vm_le(left, right, expected, vm, capsys):
    """Test VM with less-than-or-equal comparison bytecode."""
    bytecode = [
        Opcode.PUSH.value,
        left,
        Opcode.PUSH.value,
        right,
        Opcode.LE.value,
        Opcode.PRINT.value,
        Opcode.HALT.value,
    ]
    vm.run(bytecode)
    captured = capsys.readouterr()
    assert captured.out == expected


@pytest.mark.parametrize(
    "left,right,expected", [(5, 3, "1\n"), (3, 5, "1\n"), (3, 3, "0\n")]
)
def test_vm_neq(left, right, expected, vm, capsys):
    """Test VM with not-equal comparison bytecode."""
    bytecode = [
        Opcode.PUSH.value,
        left,
        Opcode.PUSH.value,
        right,
        Opcode.NEQ.value,
        Opcode.PRINT.value,
        Opcode.HALT.value,
    ]
    vm.run(bytecode)
    captured = capsys.readouterr()
    assert captured.out == expected


def test_vm_jmp(vm, capsys):
    """Test VM with jump bytecode."""
    bytecode = [
        Opcode.JMP.value,
        5,
        Opcode.PUSH.value,
        0,
        Opcode.PRINT.value,
        Opcode.PUSH.value,
        1,
        Opcode.PRINT.value,
        Opcode.HALT.value,
    ]
    vm.run(bytecode)
    captured = capsys.readouterr()
    assert captured.out == "1\n"


def test_vm_jz(vm, capsys):
    """Test VM with jump if zero bytecode."""
    bytecode = [
        Opcode.PUSH.value,
        0,
        Opcode.JZ.value,
        7,
        Opcode.PUSH.value,
        0,
        Opcode.PRINT.value,
        Opcode.PUSH.value,
        1,
        Opcode.PRINT.value,
        Opcode.HALT.value,
    ]
    vm.run(bytecode)
    captured = capsys.readouterr()
    assert captured.out == "1\n"


def test_vm_jnz(vm, capsys):
    """Test VM with jump if not zero bytecode."""
    bytecode = [
        Opcode.PUSH.value,
        1,
        Opcode.JNZ.value,
        7,
        Opcode.PUSH.value,
        0,
        Opcode.PRINT.value,
        Opcode.PUSH.value,
        1,
        Opcode.PRINT.value,
        Opcode.HALT.value,
    ]
    vm.run(bytecode)
    captured = capsys.readouterr()
    assert captured.out == "1\n"


def test_vm_duplicate_top(vm, capsys):
    """Test VM with duplicate top value bytecode."""
    bytecode = [
        Opcode.PUSH.value,
        42,
        Opcode.DUP.value,
        Opcode.PRINT.value,
        Opcode.PRINT.value,
        Opcode.HALT.value,
    ]
    vm.run(bytecode)
    captured = capsys.readouterr()
    assert captured.out == "42\n42\n"


def test_vm_swap_top(vm, capsys):
    """Test VM with swap top two values bytecode."""
    bytecode = [
        Opcode.PUSH.value,
        1,
        Opcode.PUSH.value,
        2,
        Opcode.SWAP.value,
        Opcode.PRINT.value,
        Opcode.PRINT.value,
        Opcode.HALT.value,
    ]
    vm.run(bytecode)
    captured = capsys.readouterr()
    assert captured.out == "1\n2\n"


def test_vm_loop(vm, capsys):
    """Test VM with a loop that counts up from 0 to 3."""
    bytecode = [
        Opcode.PUSH.value,
        0,
        Opcode.DUP.value,
        Opcode.PRINT.value,
        Opcode.PUSH.value,
        1,
        Opcode.ADD.value,
        Opcode.DUP.value,
        Opcode.PUSH.value,
        3,
        Opcode.LT.value,
        Opcode.JNZ.value,
        2,
        Opcode.PRINT.value,
        Opcode.HALT.value,
    ]
    vm.run(bytecode)
    captured = capsys.readouterr()
    assert captured.out == "0\n1\n2\n3\n"


def test_vm_store_and_load(vm, capsys):
    """Test VM with store and load bytecode."""
    bytecode = [
        Opcode.PUSH.value,
        42,
        Opcode.STORE.value,
        0,
        Opcode.LOAD.value,
        0,
        Opcode.PRINT.value,
        Opcode.HALT.value,
    ]
    vm.run(bytecode)
    captured = capsys.readouterr()
    assert vm._memory[0] == 42
    assert captured.out == "42\n"


def test_vm_pop(vm, capsys):
    """Test VM with pop bytecode."""
    bytecode = [
        Opcode.PUSH.value,
        42,
        Opcode.PUSH.value,
        1,
        Opcode.POP.value,
        Opcode.PRINT.value,
        Opcode.HALT.value,
    ]
    vm.run(bytecode)
    captured = capsys.readouterr()
    assert captured.out == "42\n"
    assert vm._stack.is_empty()


def test_vm_invalid_memory_address_load(vm):
    """Test VM with invalid memory addresses for LOAD."""
    bytecode = [
        Opcode.LOAD.value,
        300,
        Opcode.HALT.value,
    ]
    with pytest.raises(VirtualMachineError):
        vm.run(bytecode)


def test_vm_invalid_memory_address_store(vm):
    """Test VM with invalid memory addresses for STORE."""
    bytecode = [
        Opcode.PUSH.value,
        1,
        Opcode.STORE.value,
        300,
        Opcode.HALT.value,
    ]
    with pytest.raises(VirtualMachineError):
        vm.run(bytecode)

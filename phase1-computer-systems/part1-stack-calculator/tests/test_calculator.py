from calculator import (
    Calculator,
    CalculatorError,
    InsufficientOperandsError,
    TooManyOperandsError,
)
import pytest


@pytest.fixture
def calc():
    """Fixture to create a Calculator instance."""
    return Calculator()


def test_simple_addition(calc):
    """Test simple addition operation."""
    assert calc.evaluate("3 4 +") == 7.0


def test_simple_subtraction(calc):
    """Test simple subtraction operation."""
    assert calc.evaluate("10 4 -") == 6.0


def test_simple_multiplication(calc):
    """Test simple multiplication operation."""
    assert calc.evaluate("3 5 *") == 15.0


def test_simple_division(calc):
    """Test simple division operation."""
    assert calc.evaluate("20 4 /") == 5.0


def test_complex_expression(calc):
    """Test a more complex expression."""
    assert calc.evaluate("3 4 + 2 * 7 /") == 2.0


def test_division_by_zero_error(calc):
    """Test division by zero raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        calc.evaluate("10 0 /")


def test_too_many_operands_error(calc):
    """Test that too many operands raises TooManyOperandsError."""
    with pytest.raises(TooManyOperandsError):
        calc.evaluate("3 3")


def test_insufficient_operands_error(calc):
    """Test that insufficient operands raises InsufficientOperandsError."""
    with pytest.raises(InsufficientOperandsError):
        calc.evaluate("3 +")

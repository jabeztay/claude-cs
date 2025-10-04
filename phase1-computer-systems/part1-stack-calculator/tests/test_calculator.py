import math

import pytest
from calculator import (
    Calculator,
    CalculatorError,
    InsufficientOperandsError,
    TooManyOperandsError,
)


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


def test_constant_evaluation(calc):
    """Test that constants evaluate correctly."""
    assert calc.evaluate("pi") == math.pi
    assert calc.evaluate("e") == math.e


def test_trigonometric_functions(calc):
    """Test trigonometric functions."""
    assert math.isclose(calc.evaluate("0 sin"), 0.0)
    assert math.isclose(calc.evaluate("0 cos"), 1.0)
    assert math.isclose(calc.evaluate("0 tan"), 0.0)
    assert math.isclose(calc.evaluate("pi 2 / sin"), 1.0, rel_tol=1e-9)
    assert math.isclose(calc.evaluate("pi cos"), -1.0, rel_tol=1e-9)
    assert calc.evaluate("pi sin") == math.sin(math.pi)

def test_log_exp_sqrt_functions(calc):
    """Test log, exp, and sqrt functions."""
    assert math.isclose(calc.evaluate("1 log"), 0.0)
    assert math.isclose(calc.evaluate("1 exp"), math.e)
    assert math.isclose(calc.evaluate("4 sqrt"), 2.0)


def test_sqrt_log_negative_number_errors(calc):
    """Test that sqrt and log of negative numbers raise ValueError."""
    with pytest.raises(ValueError):
        calc.evaluate("-4 sqrt")

    with pytest.raises(ValueError):
        calc.evaluate("-1 log")

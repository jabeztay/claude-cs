import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from calculator import Calculator

import pytest


def test_basic_operations():
    calc = Calculator()
    calc.execute("3 4 +")
    assert calc.result() == 7


def test_persistent_stack():
    calc = Calculator()
    calc.execute("5 3 +")
    calc.execute("2 *")
    assert calc.result() == 16


def test_variables():
    calc = Calculator()
    calc.execute("10 x =")
    assert calc.result() == 10
    calc.clear_stack()
    calc.execute("x 5 +")
    assert calc.result() == 15


def test_empty_calculator():
    calc = Calculator()
    assert calc.result() == 0


def test_errors():
    with pytest.raises(ValueError, match="Invalid variable name 'hello'"):
        calc = Calculator()
        calc.execute("10 hello =")

    with pytest.raises(ValueError, match="Undefined variable 'x'"):
        calc = Calculator()
        calc.execute("x x +")

    with pytest.raises(ValueError, match="Stack currently has 2"):
        calc = Calculator()
        calc.execute("10 10 10 +")
        calc.result()

    with pytest.raises(ValueError, match="requires 2.*but stack only has 1"):
        calc = Calculator()
        calc.execute("10 +")


def test_math():
    calc = Calculator()
    calc.execute("0 sin")
    assert calc.result() == 0

    calc.execute("cos")
    assert calc.result() == 1

    calc.execute("log")
    assert calc.result() == 0


def test_clear_variables():
    calc = Calculator()
    calc.execute("10 x =")
    calc.clear_stack()
    calc.execute("x x *")
    assert calc.result() == 100
    calc.clear_variables()

    with pytest.raises(ValueError, match="Undefined variable 'x'"):
        calc.execute("x *")

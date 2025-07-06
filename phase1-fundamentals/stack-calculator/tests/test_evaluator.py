import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from evaluator import evaluate

import pytest


def test_evaluator_success():
    assert evaluate("3 4 +") == 7
    assert evaluate("15 7 1 1 + - / 3 * 2 1 1 + + -") == 5
    assert evaluate("5 neg") == -5
    assert evaluate("9 sqrt") == 3.0
    assert evaluate("42") == 42
    assert evaluate("2 3 pow") == 8
    assert evaluate("10 2 /") == 5
    assert evaluate("6 7 *") == 42


def test_evaluator_errors():
    with pytest.raises(ValueError):
        evaluate("3 +")

    with pytest.raises(ValueError):
        evaluate("3 invalidop")

    with pytest.raises(ValueError):
        evaluate("")

    with pytest.raises(ValueError):
        evaluate("3 4 5")

    with pytest.raises(ZeroDivisionError):
        evaluate("1 0 /")

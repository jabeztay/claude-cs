import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from tokenizer import tokenize


def test_tokenizer_returns_empty_array():
    result = tokenize("")
    assert result == []
    result = tokenize(" ")
    assert result == []


def test_tokenizer_returns_clean_striped_array():
    result = tokenize(" 3  4 + 2 * ")
    assert result == ["3", "4", "+", "2", "*"]

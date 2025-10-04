import pytest
from tokenizer import EmptyInputError, InvalidTokenError, Token, TokenType, tokenize


def test_empty_input():
    """Test that empty inputs raise EmptyInputError"""
    with pytest.raises(EmptyInputError):
        tokenize("")

    with pytest.raises(EmptyInputError):
        tokenize("   ")


def test_numbers():
    """Test that numbers are tokenized correctly"""
    assert tokenize("42") == [Token(TokenType.NUMBER, 42.0)]
    assert tokenize("3.14") == [Token(TokenType.NUMBER, 3.14)]
    assert tokenize("-7") == [Token(TokenType.NUMBER, -7.0)]
    assert tokenize("0") == [Token(TokenType.NUMBER, 0.0)]


def test_operators():
    """Test that operators are tokenized correctly"""
    assert tokenize("+") == [Token(TokenType.OPERATOR, "+")]
    assert tokenize("-") == [Token(TokenType.OPERATOR, "-")]
    assert tokenize("*") == [Token(TokenType.OPERATOR, "*")]
    assert tokenize("/") == [Token(TokenType.OPERATOR, "/")]
    assert tokenize("sin") == [Token(TokenType.OPERATOR, "sin")]
    assert tokenize("cos") == [Token(TokenType.OPERATOR, "cos")]
    assert tokenize("tan") == [Token(TokenType.OPERATOR, "tan")]
    assert tokenize("log") == [Token(TokenType.OPERATOR, "log")]
    assert tokenize("exp") == [Token(TokenType.OPERATOR, "exp")]
    assert tokenize("sqrt") == [Token(TokenType.OPERATOR, "sqrt")]


def test_constants():
    """Test that constants are tokenized correctly"""
    assert tokenize("pi") == [Token(TokenType.CONSTANT, "pi")]
    assert tokenize("e") == [Token(TokenType.CONSTANT, "e")]


def test_mixed_expression():
    """Test that a mixed expression is tokenized correctly"""
    expression = "3 4 + 2 * 7 /"
    expected_tokens = [
        Token(TokenType.NUMBER, 3.0),
        Token(TokenType.NUMBER, 4.0),
        Token(TokenType.OPERATOR, "+"),
        Token(TokenType.NUMBER, 2.0),
        Token(TokenType.OPERATOR, "*"),
        Token(TokenType.NUMBER, 7.0),
        Token(TokenType.OPERATOR, "/"),
    ]
    assert tokenize(expression) == expected_tokens


def test_invalid_tokens():
    """Test that invalid tokens raise InvalidTokenError"""
    with pytest.raises(InvalidTokenError):
        tokenize("3 4 &")

    with pytest.raises(InvalidTokenError):
        tokenize("hello world")

    with pytest.raises(InvalidTokenError):
        tokenize("5 6 ^")

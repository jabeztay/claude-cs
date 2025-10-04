import pytest
from tokenizer import (
    EmptyInputError,
    InvalidTokenError,
    Token,
    TokenType,
    check_variable_name,
    tokenize,
)


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
    assert tokenize("STO") == [Token(TokenType.OPERATOR, "STO")]


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
        tokenize("5 6 ^")

    with pytest.raises(InvalidTokenError):
        tokenize("v@r1")


def test_variable_name_check():
    """Test that variable names are checked correctly"""
    assert check_variable_name("var1") is True
    assert check_variable_name("myVar") is True
    assert check_variable_name("x") is True
    assert check_variable_name("var_1") is False
    assert check_variable_name("1var") is False
    assert check_variable_name("var-name") is False
    assert check_variable_name("var$name") is False
    assert check_variable_name("v@r") is False
    assert check_variable_name("&") is False
    assert check_variable_name("^") is False
    assert check_variable_name("pi") is False
    assert check_variable_name("e") is False
    assert check_variable_name("+") is False


def test_valid_variable_token():
    """Test that variable tokens are handled correctly"""
    assert tokenize("hello world") == [
        Token(TokenType.VARIABLE, "hello"),
        Token(TokenType.VARIABLE, "world"),
    ]
    assert tokenize("var1") == [Token(TokenType.VARIABLE, "var1")]

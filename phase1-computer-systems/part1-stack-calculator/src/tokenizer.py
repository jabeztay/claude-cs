from dataclasses import dataclass
from enum import Enum

VALID_OPERATORS = {"+", "-", "*", "/"}
RESERVED_CONSTANTS = {"pi", "e"}


class TokenType(Enum):
    NUMBER = "NUMBER"
    OPERATOR = "OPERATOR"
    CONSTANT = "CONSTANT"


@dataclass
class Token:
    type: TokenType
    value: float | str


class TokenizerError(Exception):
    """Base tokenizer error"""

    pass


class InvalidTokenError(TokenizerError):
    """Raised when an invalid token is encountered"""

    pass


class EmptyInputError(TokenizerError):
    """Raised when the input string is empty"""

    pass


def tokenize(expression: str) -> list[Token]:
    """Tokenizes a postfix expression into a list of Tokens."""
    expression = expression.strip()
    if not expression:
        raise EmptyInputError("Input expression is empty.")

    tokens = expression.split()
    result = []

    for token in tokens:
        try:
            value = float(token)
            result.append(Token(TokenType.NUMBER, value))
        except ValueError:
            if token in VALID_OPERATORS:
                result.append(Token(TokenType.OPERATOR, token))
            elif token in RESERVED_CONSTANTS:
                result.append(Token(TokenType.CONSTANT, token))
            else:
                raise InvalidTokenError(f"Invalid token: {token}")

    return result

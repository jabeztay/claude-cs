import math

from stack import Stack
from tokenizer import TokenType, tokenize

OPERATORS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}

CONSTANTS = {
    "pi": math.pi,
    "e": math.e,
}


class CalculatorError(Exception):
    """Base calculator error."""

    pass


class InsufficientOperandsError(CalculatorError):
    """Raised when there are not enough operands for an operation."""

    pass


class TooManyOperandsError(CalculatorError):
    """Raised when there are too many operands left after evaluation."""

    pass


class Calculator:

    @staticmethod
    def evaluate(expression: str) -> float:
        """Evaluates a postfix expressions and returns the result."""
        tokens = tokenize(expression)
        stack = Stack()

        for token in tokens:
            if token.type == TokenType.NUMBER:
                stack.push(token.value)
            elif token.type == TokenType.CONSTANT:
                stack.push(CONSTANTS[token.value])
            elif token.type == TokenType.OPERATOR:
                if stack.size() < 2:
                    raise InsufficientOperandsError(
                        "Not enough operands for operation."
                    )
                b = stack.pop()
                a = stack.pop()

                result = OPERATORS[token.value](a, b)

                stack.push(result)

        if stack.size() > 1:
            raise TooManyOperandsError("Too many operands left after evaluation.")
        return stack.peek()

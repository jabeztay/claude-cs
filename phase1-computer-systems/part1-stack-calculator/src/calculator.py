import math

from stack import Stack
from tokenizer import TokenType, tokenize

OPERATORS = {
    "+": (2, lambda a, b: a + b),
    "-": (2, lambda a, b: a - b),
    "*": (2, lambda a, b: a * b),
    "/": (2, lambda a, b: a / b),
    "sin": (1, lambda a: math.sin(a)),
    "cos": (1, lambda a: math.cos(a)),
    "tan": (1, lambda a: math.tan(a)),
    "log": (1, lambda a: math.log(a)),
    "exp": (1, lambda a: math.exp(a)),
    "sqrt": (1, lambda a: math.sqrt(a)),
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
                arity, operation = OPERATORS[token.value]
                if stack.size() < arity:
                    raise InsufficientOperandsError(
                        f"Not enough operands for '{token.value}' operation."
                    )

                result = None
                if arity == 2:
                    b = stack.pop()
                    a = stack.pop()
                    result = operation(a, b)
                elif arity == 1:
                    a = stack.pop()
                    result = operation(a)

                stack.push(result)

        if stack.size() > 1:
            raise TooManyOperandsError("Too many operands left after evaluation.")
        return stack.peek()


if __name__ == "__main__":
    print(Calculator.evaluate("pi sin"))  # Example usage

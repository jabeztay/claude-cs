import math
from dataclasses import dataclass

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


@dataclass
class REPLResult:
    output: str | None
    quit: bool = False


class CalculatorError(Exception):
    """Base calculator error."""

    pass


class InsufficientOperandsError(CalculatorError):
    """Raised when there are not enough operands for an operation."""

    pass


class TooManyOperandsError(CalculatorError):
    """Raised when there are too many operands left after evaluation."""

    pass


class UndefinedVariableError(CalculatorError):
    """Raised when a variable is used before being defined."""

    pass


class Calculator:

    def __init__(self) -> None:
        """Initializes the calculator."""
        self._vars = {}
        self._ans = 0.0

    def evaluate(self, expression: str) -> float:
        """Evaluates a postfix expressions and returns the result."""
        tokens = tokenize(expression)
        stack = Stack()

        last_token_consumed = -1
        for i, token in enumerate(tokens):
            if last_token_consumed >= i:
                continue

            if token.type == TokenType.NUMBER:
                stack.push(token.value)

            elif token.type == TokenType.CONSTANT:
                stack.push(CONSTANTS[token.value])

            elif token.type == TokenType.OPERATOR:
                if token.value == "STO":
                    if stack.size() < 1:
                        raise InsufficientOperandsError(
                            "Not enough operands for 'STO' operation."
                        )
                    last_token_consumed = i + 1
                    if last_token_consumed >= len(tokens):
                        raise CalculatorError(
                            "No variable provided for 'STO' operation."
                        )
                    next_token = tokens[last_token_consumed]
                    if next_token.type != TokenType.VARIABLE:
                        raise CalculatorError(
                            f"Expected variable after 'STO', got '{next_token.value}'."
                        )
                    if next_token.value == "ans":
                        raise CalculatorError("Cannot overwrite reserved name 'ans'.")
                    a = stack.peek()
                    self._vars[next_token.value] = a

                else:
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

            elif token.type == TokenType.VARIABLE:
                if token.value == "ans":
                    stack.push(self._ans)
                elif token.value in self._vars:
                    stack.push(self._vars[token.value])
                else:
                    raise UndefinedVariableError(
                        f"Variable '{token.value}' is not defined."
                    )

        if stack.size() > 1:
            raise TooManyOperandsError(
                f"Too many operands left after evaluation. {stack}"
            )

        return stack.peek()

    def repl(self) -> None:
        """Starts a REPL for the calculator."""
        print("Postfix Calculator REPL. Type 'help' for commands.")

        while True:
            try:
                user_input = input("> ").strip()

                if not user_input:
                    continue

                result = self.handle_input(user_input)

                if result.quit:
                    print("Exiting calculator. Goodbye!")
                    break

                if result.output:
                    print(result.output)

            except CalculatorError as e:
                print(f"Error: {e}")
            except KeyboardInterrupt:
                print("\nExiting calculator. Goodbye!")
                break
            except Exception as e:
                print(f"Unexpected error: {e}")

    def handle_input(self, input_str: str) -> REPLResult:
        """Processes user input and returns result.
        Assumes that input_str is non-empty and stripped.
        """
        if input_str == "exit" or input_str == "quit":
            return REPLResult(output=None, quit=True)
        elif input_str == "clear":
            self._vars.clear()
            return REPLResult(output="All variables cleared.", quit=False)
        elif input_str == "help":
            help_text = (
                "Supported commands:\n"
                "- exit, quit: Exit the calculator.\n"
                "- clear: Clear all stored variables.\n"
                "- help: Show this help message.\n"
                "- vars: List all stored variables.\n"
                "You can also enter postfix expressions to evaluate them."
            )
            return REPLResult(output=help_text, quit=False)
        elif input_str == "vars":
            if not self._vars:
                return REPLResult(output="No variables defined.", quit=False)
            vars_list = "\n".join(f"{k}: {v}" for k, v in self._vars.items())
            return REPLResult(output=vars_list, quit=False)
        else:
            result = self.evaluate(input_str)
            self._ans = result
            return REPLResult(output=str(result), quit=False)


if __name__ == "__main__":
    calc = Calculator()
    calc.repl()

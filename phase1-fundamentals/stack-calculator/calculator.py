from stack import Stack
from tokenizer import tokenize
from numbers import Number
import math


class Calculator:
    OPERATORS = {
        # function, operand_count
        '+': (lambda x, y: x + y, 2),
        '-': (lambda x, y: x - y, 2),
        '*': (lambda x, y: x * y, 2),
        '/': (lambda x, y: x / y, 2),
        'neg': (lambda x: -x, 1),
        'sqrt': (lambda x: x ** 0.5, 1),
        'pow': (lambda x, y: x ** y, 2),
        'sin': (math.sin, 1),
        'cos': (math.cos, 1),
        'tan': (math.tan, 1),
        'log': (math.log, 1),
    }

    def __init__(self):
        self.stack = Stack()
        self.variables = {}

    def execute(self, expression: str):
        tokens = tokenize(expression)
        i = 0

        while i < len(tokens):

            token = tokens[i]

            if token in self.OPERATORS:
                func, needed_operands = self.OPERATORS[token]

                if len(self.stack) < needed_operands:
                    raise ValueError(f"Operator '{token}' requires {needed_operands}, but stack only has {len(self.stack)}")

                operands = [self.stack.pop() for _ in range(needed_operands)]

                self.stack.push(func(*operands[::-1]))

            elif self._is_variable_name(token):
                if i + 1 < len(tokens) and tokens[i + 1] == "=":
                    self.variables[token] = self.stack.peek()
                    i += 1
                else:
                    self.stack.push(self._fetch_stored_value(token))

            else:
                self.stack.push(float(token))

            i += 1

    def _is_variable_name(self, token: str) -> bool:
        try:
            float(token)
            return False
        except ValueError:
            if token.isalpha() and len(token) == 1:
                return True
        raise ValueError(f"Invalid variable name '{token}'")

    def _fetch_stored_value(self, token: str) -> Number:
        try:
            return self.variables[token]
        except KeyError:
            raise ValueError(f"Undefined variable '{token}'")

    def result(self) -> Number:
        if len(self.stack) == 1:
            return self.stack.peek()
        elif len(self.stack) == 0:
            return 0
        raise ValueError(f"Stack currently has {len(self.stack)} items remaining.")

    def clear_variables(self) -> None:
        self.variables = {}

    def clear_stack(self) -> None:
        self.stack = Stack()

    def display(self) -> None:
        print(self.result())

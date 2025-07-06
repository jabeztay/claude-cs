from stack import Stack
from tokenizer import tokenize
from numbers import Number

OPERATORS = {
    # function, operand_count
    '+': (lambda x, y: x + y, 2),
    '-': (lambda x, y: x - y, 2),
    '*': (lambda x, y: x * y, 2),
    '/': (lambda x, y: x / y, 2),
    'neg': (lambda x: -x, 1),
    'sqrt': (lambda x: x ** 0.5, 1),
    'pow': (lambda x, y: x ** y, 2),
}


def evaluate(expression: str) -> Number:
    tokenized_output = tokenize(expression)
    stack = Stack()
    for token in tokenized_output:

        if token in OPERATORS:
            func, needed_operands = OPERATORS[token]

            if len(stack) < needed_operands:
                raise ValueError(f"Operator '{token}' requires {needed_operands}, but stack only has {len(stack)}")

            operands = [stack.pop() for _ in range(needed_operands)]

            stack.push(func(*operands[::-1]))

        else:
            try:
                token_value = float(token)
                stack.push(token_value)
            except ValueError:
                raise ValueError(f"'{token}' is not a valid operator or number")

    if len(stack) == 1:
        return stack.pop()
    elif len(stack) == 0:
        raise ValueError(f"Insufficent operators provided")
    else:
        raise ValueError(f"Stack still contains {len(stack)} values, insufficent operators provided")

from ast_nodes import Node
from lexer import tokenize


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def parse_addition(self):
        left = self.parse_multiplication()

        while (self.current < len(self.tokens)) and \
              ((op := self.tokens[self.current][0]) in ('+', '-')):
            self.current += 1
            right = self.parse_multiplication()
            left = Node(op, left, right)

        return left

    def parse_multiplication(self):
        left = self.parse_primary()

        while (self.current < len(self.tokens)) and \
              ((op := self.tokens[self.current][0]) in ('*', '/')):
            self.current += 1
            right = self.parse_primary()
            left = Node(op, left, right)

        return left

    def parse_primary(self):
        val, val_type = self.tokens[self.current]

        if val_type == "number":
            val = int(val)
        elif val_type == "identifier":
            pass

        self.current += 1

        return Node(val)

    def parse_expression(self):
        return self.parse_addition()


if __name__ == "__main__":
    parser = Parser(tokenize("2 + 5"))
    print(parser.tokens)
    root = parser.parse_addition()
    print(root.post_order())
    parser = Parser(tokenize("5"))
    print(parser.tokens)
    root = parser.parse_addition()
    print(root.post_order())
    parser = Parser(tokenize("5 + 2 * 2"))
    print(parser.tokens)
    root = parser.parse_addition()
    print(root.post_order())
    parser = Parser(tokenize("5 + 2 / 2"))
    print(parser.tokens)
    root = parser.parse_addition()
    print(root.post_order())
    parser = Parser(tokenize("5 * 2 + 2"))
    print(parser.tokens)
    root = parser.parse_addition()
    print(root.post_order())
    parser = Parser(tokenize("1 + 2 + 3 + 4"))
    print(parser.tokens)
    root = parser.parse_addition()
    print(root.post_order())
    parser = Parser(tokenize("10 + 5 * 2"))
    print(parser.tokens)
    root = parser.parse_addition()
    print(root.post_order())

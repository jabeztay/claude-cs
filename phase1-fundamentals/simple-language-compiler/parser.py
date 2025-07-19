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

    def parse_let_statement(self):
        self.current += 1
        var_name = self.tokens[self.current]

        self.current += 1
        if not self.tokens[self.current][0] == "=":
            raise SyntaxError(f"'let' expects '=' after variable name, but received {self.tokens[self.current][0]}")

        self.current += 1
        right = self.parse_expression()

        if not self.tokens[self.current][0] == ";":
            raise SyntaxError(f"'let' expects ';' after expression, but received {self.tokens[self.current][0]}")

        return Node("let", Node(var_name[0]), right)

    def parse_print_statement(self):
        self.current += 1
        if not self.tokens[self.current][0] == "(":
            raise SyntaxError(f"'print' expects '(' after print keyword, but received {self.tokens[self.current][0]}")

        self.current += 1
        left = self.parse_expression()

        if not self.tokens[self.current][0] == ")":
            raise SyntaxError(f"'print' expects ')' after evaluating expression, but received {self.tokens[self.current][0]}")

        self.current += 1
        if not self.tokens[self.current][0] == ";":
            raise SyntaxError(f"'print' expects ';' after expression and closing parentheses, but received {self.tokens[self.current][0]}")

        return Node("print", left=left)

    def parse_input(self):
        first_token_value = self.tokens[self.current][0]
        if first_token_value == 'let':
            return self.parse_let_statement()
        elif first_token_value == 'print':
            return self.parse_print_statement()
        else:
            return self.parse_expression()

if __name__ == "__main__":
    parser = Parser(tokenize("2 + 5"))
    print(parser.tokens)
    root = parser.parse_input()
    print(root.post_order())
    parser = Parser(tokenize("5"))
    print(parser.tokens)
    root = parser.parse_input()
    print(root.post_order())
    parser = Parser(tokenize("5 + 2 * 2"))
    print(parser.tokens)
    root = parser.parse_input()
    print(root.post_order())
    parser = Parser(tokenize("5 + 2 / 2"))
    print(parser.tokens)
    root = parser.parse_input()
    print(root.post_order())
    parser = Parser(tokenize("5 * 2 + 2"))
    print(parser.tokens)
    root = parser.parse_input()
    print(root.post_order())
    parser = Parser(tokenize("1 + 2 + 3 + 4"))
    print(parser.tokens)
    root = parser.parse_input()
    print(root.post_order())
    parser = Parser(tokenize("10 + 5 * 2"))
    print(parser.tokens)
    root = parser.parse_input()
    print(root.post_order())

    parser = Parser(tokenize("let x = 42;"))
    root = parser.parse_input()
    print(root.post_order())

    parser = Parser(tokenize("let y = x * 42;"))
    root = parser.parse_input()
    print(root.post_order())

    parser = Parser(tokenize("print(x);"))
    root = parser.parse_input()
    print(root.post_order())

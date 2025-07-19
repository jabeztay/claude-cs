from lexer import tokenize
from parser import Parser
from typing import Any


class Compiler:
    @staticmethod
    def compile_tree(tree):
        post_order = tree.post_order()
        return Compiler.generate_bytecode(post_order)

    @staticmethod
    def generate_bytecode(post_order_tokens: list[Any]):
        OPERATOR_MAP = {
            '+': 'ADD',
            '-': 'SUB',
            '*': 'MUL',
            '/': 'DIV',
        }

        instructions = []
        for token in post_order_tokens:
            if isinstance(token, int):
                instructions.append(f"LOAD_CONST {token}")
            elif token in OPERATOR_MAP:
                instructions.append(OPERATOR_MAP[token])

        return instructions



if __name__ == "__main__":
    parser = Parser(tokenize("5 * 2 + 2"))
    root = parser.parse_expression()
    print(root)
    print(Compiler.compile_tree(root))
    parser = Parser(tokenize("1 + 2 + 3 + 4"))
    root = parser.parse_expression()
    print(root)
    print(Compiler.compile_tree(root))
    parser = Parser(tokenize("10 + 5 * 2"))
    root = parser.parse_expression()
    print(root)
    print(Compiler.compile_tree(root))

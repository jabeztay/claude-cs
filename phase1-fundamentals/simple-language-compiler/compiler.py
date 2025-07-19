from lexer import tokenize
from parser import Parser
from typing import Any
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../virtual-machine'))
from vm import ADD, SUB, MUL, DIV, HALT, VirtualMachine, LOAD_CONST


class Compiler:
    @staticmethod
    def compile_tree(tree):
        post_order = tree.post_order()
        return Compiler.generate_bytecode(post_order)

    @staticmethod
    def generate_bytecode(post_order_tokens: list[Any]):
        OPERATOR_MAP = {
            '+': ADD,
            '-': SUB,
            '*': MUL,
            '/': DIV,
        }

        instructions = []
        for token in post_order_tokens:
            if isinstance(token, int):
                instructions.append(LOAD_CONST)
                instructions.append(token)
            elif token in OPERATOR_MAP:
                instructions.append(OPERATOR_MAP[token])

        instructions.append(HALT)
        return instructions



if __name__ == "__main__":
    parser = Parser(tokenize("5 * 2 + 2"))
    root = parser.parse_expression()
    print(root)
    vm = VirtualMachine()
    bytecode = Compiler.compile_tree(root)
    print(bytecode)
    vm.run(bytecode)
    print(vm.stack.peek())

    parser = Parser(tokenize("1 + 2 + 3 + 4"))
    root = parser.parse_expression()
    print(root)
    vm = VirtualMachine()
    bytecode = Compiler.compile_tree(root)
    print(bytecode)
    vm.run(bytecode)
    print(vm.stack.peek())

    parser = Parser(tokenize("10 + 5 * 2"))
    root = parser.parse_expression()
    print(root)
    vm = VirtualMachine()
    bytecode = Compiler.compile_tree(root)
    print(bytecode)
    vm.run(bytecode)
    print(vm.stack.peek())

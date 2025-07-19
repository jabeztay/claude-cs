from lexer import tokenize
from parser import Parser
from typing import Any
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../virtual-machine'))
from vm import *


class Compiler:
    @staticmethod
    def compile_tree(tree):
        if tree.val == "let":
            bytecode = Compiler.compile_let_statement(tree)
        elif tree.val == "print":
            bytecode = Compiler.compile_print_statement(tree)
        else:
            post_order = tree.post_order()
            bytecode = Compiler.generate_expression_bytecode(post_order)

        bytecode.append(HALT)
        return bytecode

    @staticmethod
    def compile_let_statement(tree):
        var_name = tree.left.val

        right_post_order = tree.right.post_order()
        right_bytecode = Compiler.generate_expression_bytecode(right_post_order)

        instructions = right_bytecode + [STORE, var_name]
        return instructions

    @staticmethod
    def compile_print_statement(tree):
        left_post_order = tree.left.post_order()
        left_bytecode = Compiler.generate_expression_bytecode(left_post_order)

        instructions = left_bytecode + [PRINT]
        return instructions

    @staticmethod
    def generate_expression_bytecode(post_order_tokens: list[Any]):
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
            elif isinstance(token, str):
                instructions.append(LOAD_VAR)
                instructions.append(token)

        return instructions



if __name__ == "__main__":
    parser = Parser(tokenize("5 * 2 + 2"))
    root = parser.parse_input()
    print(root)
    vm = VirtualMachine()
    bytecode = Compiler.compile_tree(root)
    print(bytecode)
    vm.run(bytecode)
    print(vm.stack.peek())

    parser = Parser(tokenize("1 + 2 + 3 + 4"))
    root = parser.parse_input()
    print(root)
    vm = VirtualMachine()
    bytecode = Compiler.compile_tree(root)
    print(bytecode)
    vm.run(bytecode)
    print(vm.stack.peek())

    parser = Parser(tokenize("10 + 5 * 2"))
    root = parser.parse_input()
    print(root)
    vm = VirtualMachine()
    bytecode = Compiler.compile_tree(root)
    print(bytecode)
    vm.run(bytecode)
    print(vm.stack.peek())

    parser = Parser(tokenize("let x = 42;"))
    root = parser.parse_input()
    print(root)
    vm = VirtualMachine()
    bytecode = Compiler.compile_tree(root)
    print(bytecode)
    vm.run(bytecode)
    print(vm.variables)

    parser = Parser(tokenize("let x = 10 + 5;"))
    root = parser.parse_input()
    print(root)
    vm = VirtualMachine()
    bytecode = Compiler.compile_tree(root)
    print(bytecode)
    vm.run(bytecode)
    print(vm.variables)

    parser = Parser(tokenize("x * 2"))
    root = parser.parse_input()
    print(root)
    bytecode = Compiler.compile_tree(root)
    print(bytecode)
    vm.run(bytecode)
    print(vm.stack.peek())

    parser = Parser(tokenize("let x = 42;"))
    root = parser.parse_input()
    print(root)
    vm = VirtualMachine()
    bytecode = Compiler.compile_tree(root)
    print(bytecode)
    vm.run(bytecode)
    print(vm.variables)

    parser = Parser(tokenize("print(x);"))
    root = parser.parse_input()
    print(root)
    bytecode = Compiler.compile_tree(root)
    print(bytecode)
    vm.run(bytecode)

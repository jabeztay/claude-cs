from calculator import Calculator


def main():
    calc = Calculator()
    print("Stack Calculator (type 'quit' to exit, 'clear' to clear stack, 'clearvar' to clear stored variables)")

    while True:
        try:
            expr = input(">> ")
            if expr.lower() == 'quit':
                break
            elif expr.lower() == 'clear':
                calc.clear_stack()
                print("Stack is cleared")
                continue
            elif expr.lower() == 'clearvar':
                calc.clear_variables()
                print("Stored variables are cleared")
                continue
            calc.execute(expr)
            calc.display()
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()

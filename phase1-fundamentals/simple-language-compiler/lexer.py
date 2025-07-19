import re

KEYWORDS = {"let", "print"}
OPERATORS = {"+", "-", "*", "/", "="}
PUNCTUATION = {"(", ")", ";"}


def tokenize(expression: str) -> list[str]:
    tokens = re.split("([ =;+-/*\(\)])", expression)
    output = []
    for token in tokens:

        if not token.strip():
            continue

        elif token in KEYWORDS:
            type = "keyword"

        elif token in OPERATORS:
            type = "operator"

        elif token in PUNCTUATION:
            type = "punctuation"

        else:
            try:
                float(token)
                type = "number"
            except ValueError:
                type = "identifier"

        output.append((token, type))

    return output


if __name__ == "__main__":
    print(tokenize("let x = 42;"))
    print(tokenize("let x = 42 - 5;"))
    print(tokenize("let y = 99;"))
    print(tokenize("let x=42;"))
    print(tokenize("print(x);"))

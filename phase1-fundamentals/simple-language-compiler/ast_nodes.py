class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        output = f"Node(val={self.val}"
        if self.left:
            output += f", left={self.left}"
        if self.right:
            output += f", right={self.right}"
        output += ")"

        return output

    def post_order(self):
        result = []
        if self.left:
            result.extend(self.left.post_order())
        if self.right:
            result.extend(self.right.post_order())
        result.append(self.val)
        return result


if __name__ == "__main__":
    tokens = [('10', 'number'), ('+', 'operator'), ('5', 'number')]

    left = Node('10')
    right = Node('5')
    root = Node('+', left, right)

    print(root)
    root.post_order()

class BTree:
    def __init__(self, order=4, keys=None, values=None, children=None, next_leaf=None):
        self._order = order
        self._keys = [] if keys is None else keys
        self._values = [] if values is None else values
        self._children = [] if children is None else children
        self._next_leaf = next_leaf

    def is_leaf(self):
        return len(self._children) == 0

    def is_internal(self):
        return len(self._values) == 0

    def search(self, search_key):
        if self.is_leaf():
            val_index = self.binary_search_value(search_key)
            if val_index == -1:
                return None
            return self._values[val_index]
        else:
            child_index = self.binary_search_child(search_key)
            return self._children[child_index].search(search_key)

    def find_leaf(self, search_key):
        if self.is_leaf():
            return self
        else:
            child_index = self.binary_search_child(search_key)
            return self._children[child_index].find_leaf(search_key)

    def find_start_index(self, search_key):
        start, end = 0, len(self._keys)

        while start < end:
            mid = (start + end) // 2
            if self._keys[mid] < search_key:
                start = mid + 1
            else:
                end = mid

        return start

    def binary_search_child(self, search_key):
        start, end = 0, len(self._keys)

        while start < end:
            mid = (start + end) // 2
            if self._keys[mid] <= search_key:
                start = mid + 1
            else:
                end = mid

        return start

    def binary_search_value(self, search_key):
        start, end = 0, len(self._keys) - 1

        while start <= end:
            mid = (start + end) // 2
            if self._keys[mid] == search_key:
                return mid
            if self._keys[mid] < search_key:
                start = mid + 1
            else:
                end = mid - 1

        return -1

    def range_query(self, start_key, end_key):
        current_leaf = self.find_leaf(start_key)
        current_index = current_leaf.find_start_index(start_key)

        result = []

        while current_leaf is not None and current_index < len(current_leaf._keys):
            current_key = current_leaf._keys[current_index]

            if current_key > end_key:
                break

            result.append((current_leaf._keys[current_index], current_leaf._values[current_index]))

            current_index += 1
            if current_index >= len(current_leaf._keys):
                current_leaf = current_leaf._next_leaf
                current_index = 0

        return result

    def split_leaf(self):
        mid = len(self._keys) // 2

        right_node = BTree(
            order=self._order,
            keys=self._keys[mid:],
            values=self._values[mid:],
            next_leaf=self._next_leaf
        )

        self._keys = self._keys[:mid]
        self._values = self._values[:mid]
        self._next_leaf = right_node

        promoted_key = right_node._keys[0]
        return promoted_key, right_node

    def split_internal(self):
        mid = len(self._keys) // 2

        promoted_key = self._keys[mid]

        right_node = BTree(
            order=self._order,
            keys=self._keys[mid + 1:],
            children=self._children[mid + 1:]
        )

        self._keys = self._keys[:mid]
        self._children = self._children[:mid + 1]

        return promoted_key, right_node

    def insert_into_leaf(self, key, value):
        insert_index = self.find_start_index(key)

        if insert_index < len(self._keys) and self._keys[insert_index] == key:
            self._values[insert_index] = value
        else:
            self._keys.insert(insert_index, key)
            self._values.insert(insert_index, value)

    def insert_into_internal(self, promoted_key, new_node):
        insert_index = self.find_start_index(promoted_key)
        self._keys.insert(insert_index, promoted_key)
        self._children.insert(insert_index + 1, new_node)

    def insert(self, key, value):
        if self.is_leaf():
            self.insert_into_leaf(key, value)

            if len(self._keys) > self._order:
                promoted_key, new_node = self.split_leaf()
                return promoted_key, new_node
            else:
                return None, None

        else:
            child_index = self.binary_search_child(key)
            child = self._children[child_index]

            promoted_key, new_node = child.insert(key, value)

            if promoted_key is not None:
                self.insert_into_internal(promoted_key, new_node)

            if len(self._keys) > self._order:
                promoted_key, new_node = self.split_internal()
                return promoted_key, new_node
            else:
                return None, None

    def insert_key_value(self, key, value):
        promoted_key, new_node = self.insert(key, value)

        if promoted_key:
            new_root = BTree(
                order=self._order,
                keys=[promoted_key],
                children=[self, new_node]
            )

            return new_root

        return self

    def __repr__(self):
        if self.is_leaf():
            return f"Leaf(keys={self._keys}, values={self._values})"
        else:
            return f"Internal(keys={self._keys}, children={len(self._children)})"


def print_tree(node, level=0):
    """Pretty print the tree structure"""
    indent = "  " * level
    print(f"{indent}{node}")
    if node.is_internal():
        for child in node._children:
            print_tree(child, level + 1)


if __name__ == "__main__":
    btree = BTree(keys=["mango", "zebra"])
    print(btree.binary_search_child("apple"))  # 0
    print(btree.binary_search_child("mango"))  # 1
    print(btree.binary_search_child("orange"))  # 1
    print(btree.binary_search_child("zebra"))  # 2
    print(btree.binary_search_child("zoo"))  # 2
    print(btree.binary_search_value("apple"))  # -1
    print(btree.binary_search_value("mango"))  # 0
    print(btree.binary_search_value("orange"))  # -1
    print(btree.binary_search_value("zebra"))  # 1
    print(btree.binary_search_value("zoo"))  # -1

    first = BTree(keys=["apple", "banana"], values=["fruit1", "fruit2"])
    second = BTree(keys=["orange", "zebra"], values=["fruit3", "animal1"])
    first._next_leaf = second
    root = BTree(keys=["m"], children=[
        first,
        second,
    ])

    print(root.search("apple"))    # Should return "fruit1"
    print(root.search("orange"))   # Should return "fruit3"
    print(root.search("missing"))  # Should return None
    print(root.search("zzz"))      # Should return None

    print(root.find_leaf("banana"))
    print(root.find_leaf("orange"))
    print(root.find_leaf("zzz"))

    node = root.find_leaf("zzz")
    print(node.find_start_index("zebra"))
    print(node.find_start_index("zzz"))

    print(root.range_query("banana", "orange"))  # [('banana', 'fruit2'), ('orange', 'fruit3')]

    print("!!! B-Tree Insertion Test (order=3)")

    root = BTree(order=3)

    test_data = [
        ("apple", "fruit1"),
        ("banana", "fruit2"),
        ("cherry", "fruit3"),
        ("date", "fruit4"),
        ("elderberry", "fruit5"),
        ("fig", "fruit6"),
        ("grape", "fruit7"),
        ("pineapple", "fruit8"),
        ("jackfruit", "fruit9"),
        ("guava", "fruit10"),
        ("apple", "fruit11")
    ]

    for key, value in test_data:
        print(f"\nInserting: {key} -> {value}")
        root = root.insert_key_value(key, value)
        print("Tree structure:")
        print_tree(root)
        print("-" * 40)

class BTree:
    def __init__(self, keys=None, values=None, children=None, next_leaf=None):
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

    def __repr__(self):
        return f"BTree(keys={self._keys})"


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

class BPlusTree:
    def __init__(self, order=4, keys=None, values=None, children=None, next_leaf=None):
        self._order = order
        self._keys = [] if keys is None else keys
        self._values = [] if values is None else values
        self._children = [] if children is None else children
        self._next_leaf = next_leaf

    @property
    def min_keys(self):
        return self._order // 2

    @property
    def num_keys(self):
        return len(self._keys)

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
        start, end = 0, self.num_keys

        while start < end:
            mid = (start + end) // 2
            if self._keys[mid] < search_key:
                start = mid + 1
            else:
                end = mid

        return start

    def binary_search_child(self, search_key):
        start, end = 0, self.num_keys

        while start < end:
            mid = (start + end) // 2
            if self._keys[mid] <= search_key:
                start = mid + 1
            else:
                end = mid

        return start

    def binary_search_value(self, search_key):
        start, end = 0, self.num_keys - 1

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
        mid = self.num_keys // 2

        right_node = BPlusTree(
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
        mid = self.num_keys // 2

        promoted_key = self._keys[mid]

        right_node = BPlusTree(
            order=self._order,
            keys=self._keys[mid + 1:],
            children=self._children[mid + 1:]
        )

        self._keys = self._keys[:mid]
        self._children = self._children[:mid + 1]

        return promoted_key, right_node

    def insert_into_leaf(self, key, value):
        insert_index = self.find_start_index(key)

        if insert_index < self.num_keys and self._keys[insert_index] == key:
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

            if self.num_keys > self._order:
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

            if self.num_keys > self._order:
                promoted_key, new_node = self.split_internal()
                return promoted_key, new_node
            else:
                return None, None

    def insert_key_value(self, key, value):
        promoted_key, new_node = self.insert(key, value)

        if promoted_key:
            new_root = BPlusTree(
                order=self._order,
                keys=[promoted_key],
                children=[self, new_node]
            )

            return new_root

        return self

    def delete(self, key, path=None):
        if path is None:
            path = []

        if self.is_leaf():
            delete_index = self.binary_search_value(key)

            if delete_index == -1:
                return None, None
            else:
                self._keys.pop(delete_index)
                self._values.pop(delete_index)

                new_first_key = self._keys[0] if (self._keys) and (delete_index == 0) else None

            if path and self.num_keys < self.min_keys:
                parent, child_index = path[-1]
                left_sibling, right_sibling = None, None
                if child_index > 0:
                    left_sibling = parent._children[child_index - 1]
                if child_index < len(parent._children) - 1:
                    right_sibling = parent._children[child_index + 1]

                if left_sibling and left_sibling.num_keys > left_sibling.min_keys:
                    k, v = left_sibling._keys.pop(), left_sibling._values.pop()
                    self._keys.insert(0, k)
                    self._values.insert(0, v)
                    return k, None

                elif right_sibling and right_sibling.num_keys > right_sibling.min_keys:
                    k, v = right_sibling._keys.pop(0), right_sibling._values.pop(0)
                    self._keys.append(k)
                    self._values.append(v)
                    return new_first_key, "borrow_right"

                elif left_sibling:
                    left_sibling._keys.extend(self._keys)
                    left_sibling._values.extend(self._values)
                    left_sibling._next_leaf = self._next_leaf
                    return None, "merge_left"

                elif right_sibling:
                    self._keys.extend(right_sibling._keys)
                    self._values.extend(right_sibling._values)
                    self._next_leaf = right_sibling._next_leaf
                    return new_first_key, "merge_right"

                else:
                    # this case shouldnt happen
                    pass

            elif self._keys:
                return self._keys[0], None
            else:
                return None, None

        else:
            child_index = self.binary_search_child(key)
            child = self._children[child_index]
            path.append((self, child_index))

            new_first_key, merge_info = child.delete(key, path)
            path.pop()

            if new_first_key is not None and child_index > 0:
                self._keys[child_index - 1] = new_first_key

            if merge_info:
                if merge_info == "merge_left":
                    self._keys.pop(child_index - 1)
                    self._children.pop(child_index)
                elif merge_info == "merge_right":
                    self._keys.pop(child_index)
                    self._children.pop(child_index + 1)
                elif merge_info == "borrow_right":
                    right_sibling = self._children[child_index + 1]
                    new_right_first_key = right_sibling._keys[0]
                    self._keys[child_index] = new_right_first_key
                    return new_first_key, None

                if path and self.num_keys < self.min_keys:
                    parent, child_index = path[-1]
                    left_sibling, right_sibling = None, None
                    if child_index > 0:
                        left_sibling = parent._children[child_index - 1]
                    if child_index < len(parent._children) - 1:
                        right_sibling = parent._children[child_index + 1]

                    if left_sibling and left_sibling.num_keys > left_sibling.min_keys:
                        k, c = left_sibling._keys.pop(), left_sibling._children.pop()
                        parent_separator = parent._keys[child_index - 1]
                        self._keys.insert(0, parent_separator)
                        self._children.insert(0, c)
                        return k, None

                    elif right_sibling and right_sibling.num_keys > right_sibling.min_keys:
                        new_first_key, c = right_sibling._keys.pop(0), right_sibling._children.pop(0)
                        parent_separator = parent._keys[child_index]
                        self._keys.append(parent_separator)
                        self._children.append(c)
                        return new_first_key, "borrow_right"

                    elif left_sibling:
                        parent_separator = parent._keys[child_index - 1]
                        left_sibling._keys.append(parent_separator)
                        left_sibling._keys.extend(self._keys)
                        left_sibling._children.extend(self._children)
                        return None, "merge_left"

                    elif right_sibling:
                        parent_separator = parent._keys[child_index]
                        self._keys.append(parent_separator)
                        self._keys.extend(right_sibling._keys)
                        self._children.extend(right_sibling._children)
                        return new_first_key, "merge_right"

                    else:
                        # this case shouldnt happen
                        pass
                else:
                    return new_first_key, None
            else:
                return new_first_key, None

    def delete_key_value(self, key):
        new_first_key, merge_info = self.delete(key)

        if self.is_internal() and (self.num_keys == 0):
            if self._children:
                return self._children[0]

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


# if __name__ == "__main__":
#     btree = BPlusTree(keys=["mango", "zebra"])
#     print(btree.binary_search_child("apple"))  # 0
#     print(btree.binary_search_child("mango"))  # 1
#     print(btree.binary_search_child("orange"))  # 1
#     print(btree.binary_search_child("zebra"))  # 2
#     print(btree.binary_search_child("zoo"))  # 2
#     print(btree.binary_search_value("apple"))  # -1
#     print(btree.binary_search_value("mango"))  # 0
#     print(btree.binary_search_value("orange"))  # -1
#     print(btree.binary_search_value("zebra"))  # 1
#     print(btree.binary_search_value("zoo"))  # -1

#     first = BPlusTree(keys=["apple", "banana"], values=["fruit1", "fruit2"])
#     second = BPlusTree(keys=["orange", "zebra"], values=["fruit3", "animal1"])
#     first._next_leaf = second
#     root = BPlusTree(keys=["m"], children=[
#         first,
#         second,
#     ])

#     print(root.search("apple"))    # Should return "fruit1"
#     print(root.search("orange"))   # Should return "fruit3"
#     print(root.search("missing"))  # Should return None
#     print(root.search("zzz"))      # Should return None

#     print(root.find_leaf("banana"))
#     print(root.find_leaf("orange"))
#     print(root.find_leaf("zzz"))

#     node = root.find_leaf("zzz")
#     print(node.find_start_index("zebra"))
#     print(node.find_start_index("zzz"))

#     print(root.range_query("banana", "orange"))  # [('banana', 'fruit2'), ('orange', 'fruit3')]

#     print("!!! B-Plus-Tree Insertion Test (order=3)")

#     root = BPlusTree(order=3)

#     test_data = [
#         ("apple", "fruit1"),
#         ("banana", "fruit2"),
#         ("cherry", "fruit3"),
#         ("date", "fruit4"),
#         ("elderberry", "fruit5"),
#         ("fig", "fruit6"),
#         ("grape", "fruit7"),
#         ("pineapple", "fruit8"),
#         ("jackfruit", "fruit9"),
#         ("guava", "fruit10"),
#         ("apple", "fruit11")
#     ]

#     for key, value in test_data:
#         print(f"\nInserting: {key} -> {value}")
#         root = root.insert_key_value(key, value)
#         print("Tree structure:")
#         print_tree(root)
#         print("-" * 40)



def test_bplus_tree_deletion():
    """Comprehensive test cases for B+ tree deletion"""

    def create_test_tree():
        """Create a test tree with known structure"""
        # Create a tree with order 4 (min_keys = 2)
        root = BPlusTree(order=4)

        # Insert values to create a multi-level tree
        values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        for val in values:
            root = root.insert_key_value(val, f"value_{val}")

        return root

    def verify_tree_properties(node, parent_key=None):
        """Verify B+ tree properties are maintained"""
        errors = []

        # Check minimum key constraint (except for root)
        if parent_key is not None and node.num_keys < node.min_keys:
            errors.append(f"Node has {node.num_keys} keys, minimum is {node.min_keys}")

        # Check maximum key constraint
        if node.num_keys > node._order:
            errors.append(f"Node has {node.num_keys} keys, maximum is {node._order}")

        # Check key ordering
        for i in range(len(node._keys) - 1):
            if node._keys[i] >= node._keys[i + 1]:
                errors.append(f"Keys not in order: {node._keys[i]} >= {node._keys[i + 1]}")

        # For internal nodes, check children count
        if node.is_internal():
            if len(node._children) != len(node._keys) + 1:
                errors.append(f"Children count {len(node._children)} != keys count {len(node._keys)} + 1")

            # Recursively check children
            for i, child in enumerate(node._children):
                child_errors = verify_tree_properties(child, node._keys[0] if node._keys else None)
                errors.extend([f"Child {i}: {err}" for err in child_errors])

        return errors

    # Test 1: Simple deletion without underflow
    print("=== Test 1: Simple deletion without underflow ===")
    tree = create_test_tree()
    print("Before deletion:")
    print_tree(tree)

    result = tree.delete(50)  # Delete from middle of leaf
    print(f"Delete result: {result}")
    print("After deleting 50:")
    print_tree(tree)

    # Verify tree properties
    errors = verify_tree_properties(tree)
    print(f"Tree property errors: {errors}")
    print()

    # Test 2: Deletion causing borrowing from right sibling
    print("=== Test 2: Borrowing from right sibling ===")
    tree = BPlusTree(order=4)
    for val in [10, 20, 30, 40, 50]:  # Creates specific structure
        tree = tree.insert_key_value(val, f"value_{val}")

    print("Before deletion:")
    print_tree(tree)

    result = tree.delete(10)  # Should cause borrowing
    print(f"Delete result: {result}")
    print("After deleting 10:")
    print_tree(tree)
    print()

    # Test 3: Deletion causing borrowing from left sibling
    print("=== Test 3: Borrowing from left sibling ===")
    tree = BPlusTree(order=4)
    for val in [10, 20, 30, 40, 50]:
        tree = tree.insert_key_value(val, f"value_{val}")

    print("Before deletion:")
    print_tree(tree)

    result = tree.delete(50)  # Should cause borrowing from left
    print(f"Delete result: {result}")
    print("After deleting 50:")
    print_tree(tree)
    print()

    # Test 4: Deletion causing merge with left sibling
    print("=== Test 4: Merge with left sibling ===")
    tree = BPlusTree(order=4)
    for val in [10, 20, 30, 40]:
        tree = tree.insert_key_value(val, f"value_{val}")

    print("Before deletion:")
    print_tree(tree)

    result = tree.delete(40)  # Should cause merge
    print(f"Delete result: {result}")
    print("After deleting 40:")
    print_tree(tree)
    print()

    # Test 5: Deletion causing merge with right sibling
    print("=== Test 5: Merge with right sibling ===")
    tree = BPlusTree(order=4)
    for val in [10, 20, 30, 40]:
        tree = tree.insert_key_value(val, f"value_{val}")

    print("Before deletion:")
    print_tree(tree)

    result = tree.delete(10)  # Should cause merge
    print(f"Delete result: {result}")
    print("After deleting 10:")
    print_tree(tree)
    print()

    # Test 6: Cascading deletion (deletion causes multiple levels of rebalancing)
    print("=== Test 6: Cascading deletion ===")
    tree = create_test_tree()

    # Delete multiple keys to force cascading
    keys_to_delete = [10, 20, 30]
    print("Original tree:")
    print_tree(tree)

    for key in keys_to_delete:
        print(f"\nDeleting {key}:")
        result = tree.delete(key)
        print(f"Delete result: {result}")
        print_tree(tree)

        errors = verify_tree_properties(tree)
        if errors:
            print(f"Tree property errors after deleting {key}: {errors}")

        validate_tree_structure(tree)
    print()

    # Test 7: Edge case - delete from single key tree
    print("=== Test 7: Delete from single key tree ===")
    tree = BPlusTree(order=4)
    tree = tree.insert_key_value(42, "value_42")

    print("Before deletion:")
    print_tree(tree)

    result = tree.delete(42)
    print(f"Delete result: {result}")
    print("After deleting 42:")
    print_tree(tree)
    print()

    # Test 8: Delete non-existent key
    print("=== Test 8: Delete non-existent key ===")
    tree = create_test_tree()

    result = tree.delete(999)  # Key doesn't exist
    print(f"Delete non-existent key result: {result}")
    print("Tree should be unchanged:")
    print_tree(tree)
    print()

    # Test 9: Sequential deletion to empty tree
    print("=== Test 9: Sequential deletion to empty tree ===")
    tree = BPlusTree(order=4)
    values = [10, 20, 30]
    for val in values:
        tree = tree.insert_key_value(val, f"value_{val}")

    print("Starting tree:")
    print_tree(tree)

    for val in values:
        print(f"\nDeleting {val}:")
        result = tree.delete(val)
        print(f"Delete result: {result}")
        print_tree(tree)
    print()

    # Test 10: Range query after deletions
    print("=== Test 10: Range query verification ===")
    tree = create_test_tree()

    # Delete some values
    tree.delete(30)
    tree.delete(70)

    print("Tree after deleting 30 and 70:")
    print_tree(tree)

    # Test range query
    range_result = tree.range_query(25, 75)
    print(f"Range query (25-75): {range_result}")

    # Verify search functionality
    for key in [20, 30, 40, 70, 80]:  # Mix of existing and deleted keys
        result = tree.search(key)
        print(f"Search {key}: {result}")

def delete_key_value(tree, key):
    """Helper function that mimics the public interface"""
    result = tree.delete(key)
    # Handle root becoming empty or height reduction
    # This would be part of your public delete_key_value method
    return tree

def validate_tree_structure(node, level=0):
    """Check if all nodes at same level have same type"""
    if node.is_internal():
        child_types = [child.is_leaf() for child in node._children]
        if not all(t == child_types[0] for t in child_types):
            print(f"ERROR at level {level}: Mixed child types!")
            print(f"Children types: {['Leaf' if t else 'Internal' for t in child_types]}")

        for child in node._children:
            validate_tree_structure(child, level + 1)

# Run the tests
if __name__ == "__main__":
    test_bplus_tree_deletion()

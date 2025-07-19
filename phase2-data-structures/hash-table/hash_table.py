from hash_functions import simple_string_hash


class HashTable:
    def __init__(self, initial_size=19, hash_func=simple_string_hash):
        self._size = initial_size
        self._hashtable = [[] for _ in range(initial_size)]
        self.hash_func = hash_func
        self._num_items = 0

    def _get_key_hash(self, key):
        key_hash = self.hash_func(key)
        key_hash = key_hash % self._size
        return key_hash

    def _find_key_index(self, key):
        key_hash = self._get_key_hash(key)
        for i in range(len(self._hashtable[key_hash])):
            if self._hashtable[key_hash][i][0] == key:
                return i, key_hash
        return None, key_hash

    def _get_load_factor(self):
        return self._num_items / self._size

    def _is_prime(self, n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False

        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False

        return True

    def _next_prime(self):
        new_size = self._size * 2 - 1
        prime = False
        while not prime:
            new_size += 2
            prime = self._is_prime(new_size)
        return new_size

    def _resize(self):
        old_hashtable = self._hashtable
        self._size = self._next_prime()
        self._hashtable = [[] for _ in range(self._size)]

        for bucket in old_hashtable:
            for k, v in bucket:
                key_hash = self._get_key_hash(k)
                self._hashtable[key_hash].append((k, v))

    def put(self, key, value):
        key_index, key_hash = self._find_key_index(key)
        if key_index is not None:
            self._hashtable[key_hash].pop(key_index)
        else:
            self._num_items += 1
        self._hashtable[key_hash].append((key, value))

        if self._get_load_factor() >= 0.75:
            self._resize()

    def get(self, key):
        key_index, key_hash = self._find_key_index(key)
        if key_index is not None:
            return self._hashtable[key_hash][key_index][1]

        raise KeyError(f"Key '{key}' not found")

    def delete(self, key):
        key_index, key_hash = self._find_key_index(key)
        if key_index is not None:
            self._hashtable[key_hash].pop(key_index)
            self._num_items -= 1
            return

        raise KeyError(f"Key '{key}' not found")


if __name__ == "__main__":
    # ht = HashTable(19)
    # ht.put("jabez", 12345)
    # print(ht._hashtable)
    # ht.put("jabez", 67890)
    # print(ht._hashtable)

    # print(ht.get("jabez"))
    # # print(ht.get("missing"))

    # print(ht.delete("jabez"))
    # print(ht.delete("missing"))


    ht = HashTable(7)
    for i in range(20):
        ht.put(f"key{i}", i * 10)
        print(f"Added key{i}: Items={ht._num_items}, Size={ht._size}, Load={ht._get_load_factor():.2f}")

    print(ht.get("key5"))
    ht.delete("key10")
    print(f"After delete: Items={ht._num_items}")

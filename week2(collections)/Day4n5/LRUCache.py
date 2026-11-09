
from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity):
        self.max_cap = capacity
        self.cache = OrderedDict()

    def get(self, key):

        if key not in self.cache:
            return -1

        # Mark key as recently used
        self.cache.move_to_end(key)

        return self.cache[key]

    def put(self, key, value):

        # If key already exists, remove old entry
        if key in self.cache:
            del self.cache[key]

        # Insert as most recently used
        self.cache[key] = value

        # Remove least recently used entry
        if len(self.cache) > self.max_cap:
            self.cache.popitem(last=False)

    def main(self):

        self.put(1, 10)
        self.put(2, 20)

        print("Cache:", self.cache)

        print("Get 1:", self.get(1))

        print("Cache after get(1):", self.cache)

        self.put(3, 30)

        print("Cache after put(3,30):", self.cache)

        print("Get 2:", self.get(2))

        self.put(4, 40)

        print("Cache after put(4,40):", self.cache)

        print("Get 1:", self.get(1))
        print("Get 3:", self.get(3))
        print("Get 4:", self.get(4))


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.main()

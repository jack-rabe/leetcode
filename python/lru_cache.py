# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists,
# otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists.
# Otherwise, add the key-value pair to the cache. If the number of keys exceeds
# the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.


class LRUCache(object):
    def __init__(self, capacity):
        self.cache = {}
        self.order = []
        self.space = capacity

    def get(self, key):
        if key in self.cache:
            self.order.remove(key)
            self.order.insert(0, key)
            return self.cache[key]

        return -1

    def put(self, key, value):
        if self.space > 0 and key not in self.cache:
            self.space -= 1
        elif key not in self.cache:
            to_remove = self.order.pop()
            del self.cache[to_remove]

        if key in self.cache:
            self.order.remove(key)
        self.order.insert(0, key)
        self.cache[key] = value

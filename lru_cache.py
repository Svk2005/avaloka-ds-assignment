class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}            # key -> node
        self.head = Node()         # dummy node, most recent is after it
        self.tail = Node()         # dummy node, least recent is before it
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_front(node)
        return node.value

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        elif len(self.cache) == self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
        node = Node(key, value)
        self.cache[key] = node
        self._add_front(node)


if __name__ == "__main__":
    # Small test
    cache = LRUCache(2)
    cache.put("A", 1)
    cache.put("B", 2)
    print(cache.get("A"))   # 1, A is now most recently used
    cache.put("C", 3)       # B is evicted
    print(cache.get("B"))   # -1
    print(cache.get("C"))   # 3
    cache.put("A", 10)      # update A
    print(cache.get("A"))   # 10

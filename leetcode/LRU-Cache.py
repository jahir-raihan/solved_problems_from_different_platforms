class Node:

    def __init__(self, key, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.lru = Node(-1, -1)
        self.mru = Node(-1, -1)
        self.cache = dict()

        # Initial LL maping
        self.mru.next = self.lru
        self.lru.prev = self.mru

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)

            return node.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(Node(key, value))

        else:
            if len(self.cache) == self.cap:
                self.remove(self.lru.prev)
            self.insert(Node(key, value))

    def remove(self, node):
        del self.cache[node.key]
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        self.mru.next.prev = node
        node.prev = self.mru
        node.next = self.mru.next

        self.mru.next = node

        self.cache[node.key] = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
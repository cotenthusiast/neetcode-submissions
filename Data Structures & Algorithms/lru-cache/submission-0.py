class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node

        self.least_recent = Node()
        self.most_recent = Node()

        # Initially, the two dummy ends point to each other
        self.least_recent.next = self.most_recent
        self.most_recent.prev = self.least_recent

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        self._remove(node)
        self._insert_most_recent(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            self._remove(node)
            self._insert_most_recent(node)
            return

        node = Node(key, value)
        self.cache[key] = node
        self._insert_most_recent(node)

        if len(self.cache) > self.capacity:
            node_to_remove = self.least_recent.next

            self._remove(node_to_remove)
            del self.cache[node_to_remove.key]
            
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_most_recent(self, node):
        previous = self.most_recent.prev

        previous.next = node
        node.prev = previous

        node.next = self.most_recent
        self.most_recent.prev = node

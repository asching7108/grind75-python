# LstNode class for doubly-linked list
class ListNode:

    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        # Use two sentinel nodes so edge cases like no existing nodes are covered
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    # Add node to the end of the list
    def add(self, node: ListNode) -> None:
        prev_end = self.tail.prev
        prev_end.next = node
        node.prev = prev_end
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node: ListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        node = self.map[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            old_node = self.map[key]
            self.remove(old_node)

        # Create a new node and add to the end of the list
        node = ListNode(key, value)
        self.map[key] = node
        self.add(node)

        if len(self.map) > self.capacity:
            node_to_remove = self.head.next
            self.remove(node_to_remove)
            self.map.pop(node_to_remove.key)


# Time complexity: O(1) for both get and put
# Space complexity: O(capacity)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class HeapNode:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(0)
        curr = head
        heap = []

        # Initialize the heap
        for l in lists:
            if l:
                heapq.heappush(heap, HeapNode(l))

        while heap:
            node = heapq.heappop(heap).node
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, HeapNode(node.next))

        return head.next

# Time complexity: O(N log K) where N is the number of total nodes.
# We need log K for every heap push/pop.
# Space complexity: O(k) for the heap
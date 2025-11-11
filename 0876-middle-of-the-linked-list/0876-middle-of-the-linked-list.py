# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Recursive
    # def middleNodeHelper(self, head: ListNode, prevCount: int) -> Tuple[ListNode, int]: # returns (middleNode, nextCount)
    #     if not head:
    #         return None, 0
    #     middleNode, nextCount = self.middleNodeHelper(head.next, prevCount + 1)
    #     res = None
    #     if middleNode:
    #         res = middleNode
    #     elif prevCount - nextCount <= 1:
    #         res = head

    #     return [res, nextCount + 1]

    # def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     return self.middleNodeHelper(head, 0)[0]

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# Time complexity: O(n)
# Space complexity: O(n)
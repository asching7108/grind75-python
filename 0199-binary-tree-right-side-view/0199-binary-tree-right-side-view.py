# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        curr_queue = deque([root])
        next_queue = deque()

        right_side_found = False
        while curr_queue:
            node = curr_queue.popleft()
            if not right_side_found:
                res.append(node.val)
                right_side_found = True
            if node.right:
                next_queue.append(node.right)
            if node.left:
                next_queue.append(node.left)
            if not curr_queue:
                temp = curr_queue
                curr_queue = next_queue
                next_queue = temp
                right_side_found = False

        return res
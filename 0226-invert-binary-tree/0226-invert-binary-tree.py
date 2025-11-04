# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = \
            self.invertTree(root.right), self.invertTree(root.left)

        return root

# Time complexity: O(n)
# Space complexity: O(n) because h ∈ O(n) where h is the height of the tree
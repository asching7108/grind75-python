# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        node = root

        while node:
            # both p and q are greater than node
            if p.val > node.val and q.val > node.val:
                node = node.right
            # both p and q are lesser than node
            elif p.val < node.val and q.val < node.val:
                node = node.left
            # we have found the split node
            else:
                return node

# Time complexity: O(h) where worst case h = N, average h = logN
# Space complexity: O(1)
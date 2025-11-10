# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalancedHelper(self, root):
        # An empty tree is balanced and has height -1
        if not root:
            return True, -1

        # Check if subtrees are balanced
        leftIsBalanced, leftHeight = self.isBalancedHelper(root.left)
        if not leftIsBalanced:
            return False, 0

        rightIsBalanced, rightHeight = self.isBalancedHelper(root.right)
        if not rightIsBalanced:
            return False, 0

        return (
            abs(leftHeight - rightHeight) < 2,
            1 + max(leftHeight, rightHeight)
        )

    def isBalanced(self, root):
        return self.isBalancedHelper(root)[0]

# Time complexity: O(n)
# Space complexity: O(n)

# Top down approach is head recursion(pre-order traversal - DFS) where recursion comes first before the evaluation/processing.

# Bottom up approach is tail recursion(post-order traversal- DFS) where the evaluation/processing comes first before recursion. This will maintain a running sum because the evaluation happens before the call.
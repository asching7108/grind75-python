# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTreeHelper(self, root: Optional[TreeNode]) -> Tuple[int, int]: # returns (height, diameter)
        if not root:
            return [0, 0]

        leftHeight, leftDiameter = self.diameterOfBinaryTreeHelper(root.left)
        rightHeight, rightDiameter = self.diameterOfBinaryTreeHelper(root.right)
        
        return [
            max(leftHeight, rightHeight) + 1,
            max(leftDiameter, rightDiameter, leftHeight + rightHeight)
        ]

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.diameterOfBinaryTreeHelper(root)[1]

# Time complexity: O(n)
# Space complexity: O(n)
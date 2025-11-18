# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        currLevel = [root]
        nextLevel = []
        res = []

        while currLevel:
            list = []
            for node in currLevel:
                list.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            res.append(list)
            currLevel = nextLevel
            nextLevel = []

        return res
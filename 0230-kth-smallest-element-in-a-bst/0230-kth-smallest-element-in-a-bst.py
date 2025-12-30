# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # Recursive inorder DFS
        # def inorder(root: Optional[TreeNode]) -> List[int]:
        #     if not root:
        #         return []

        #     return inorder(root.left) + [r.val] + inorder(root.right)

        # return inorder(root)[k - 1]

        # Time complexity: O(N)
        # Space complexity: O(N)

        # Iterative inorder DFS
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left    # Go left

            root = stack.pop()
            # Visit node
            k -= 1
            if not k:
                return root.val
            root = root.right    # Go right

        # Time complexity: O(H + k), which results in O(logN+k) for the balanced tree
        # and O(N+k) for a completely unbalanced tree
        # Space complexity: O(H)
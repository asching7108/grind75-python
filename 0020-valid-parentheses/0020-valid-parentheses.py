class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mappings = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in mappings:
                if not stack or stack.pop() != mappings[char]:
                    return False
            else:
                stack.append(char)
        return not stack

# Time complexity: O(n)
# Space complexity: O(n)
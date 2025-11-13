class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 0
        charIndices = {}

        left = 0
        for right in range(n):
            if s[right] in charIndices:
                # We need max() here so we don't move left back to
                # an already discarded substring
                left = max(charIndices[s[right]] + 1, left)
            res = max(res, right - left + 1)
            charIndices[s[right]] = right
            print(left, right)

        return res

# Time complexity: O(n)
# Space complexity: O(min(m, n)) where m is the size of the charset
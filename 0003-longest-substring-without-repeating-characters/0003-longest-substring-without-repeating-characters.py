class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 0
        charToNextIndex = {}

        left = 0
        for right in range(n):
            if s[right] in charToNextIndex:
                left = max(charToNextIndex[s[right]], left)
            res = max(res, right - left + 1)
            charToNextIndex[s[right]] = right + 1
            print(left, right)

        return res

# Time complexity: O(n)
# Space complexity: O(min(m, n)) where m is the size of the charset
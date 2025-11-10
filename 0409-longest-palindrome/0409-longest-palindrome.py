class Solution:
    def longestPalindrome(self, s: str) -> int:
        chars = collections.Counter(s)
        res = 0

        for i in chars.values():
            if i % 2 == 0:
                res += i
            else:
                res += i - 1
                if res % 2 == 0:
                    res += 1

        return res

# Time complexity: O(n)
# Space complexity: O(n)
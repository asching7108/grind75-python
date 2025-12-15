class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = [0, 0]

        def expand(left, right) -> int:
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1

            return [left + 1, right - 1]

        # Find the longest palindrome starting from each char as center
        for i in range(1, n):
            ans = max([ans, expand(i - 1, i), expand(i, i)], key=lambda s: s[1] - s[0])

        return s[ans[0]:ans[1] + 1]

# Time complexity: O(n^2)
# Space complexity: O(1)
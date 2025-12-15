class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ''

        def findPalindrome(left, right) -> str:
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left + 1:right]

        # Find the longest palindrome starting from each char as center
        for i in range(1, n):
            # Palindrome length is even
            ans = max([ans, findPalindrome(i - 1, i), findPalindrome(i, i)], key=len)

        return ans

# Time complexity: O(n)
# Space complexity: O(1)
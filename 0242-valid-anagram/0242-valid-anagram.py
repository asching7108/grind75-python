class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chars = {}
        for ch in s:
            chars[ch] = chars.get(ch, 0) + 1
        for ch in t:
            if ch not in chars:
                return False
            chars[ch] -= 1
            if chars[ch] < 0:
                return False
        return True

# Time complexity: O(n)
# Space complexity: O(1)
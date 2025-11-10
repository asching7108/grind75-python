class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chars = {}

        for ch in magazine:
            chars[ch] = chars.get(ch, 0) + 1

        for ch in ransomNote:
            if ch not in chars or not chars[ch]:
                return False

            chars[ch] -= 1

        return True
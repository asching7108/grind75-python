class Solution:
    def minWindow(self, s: str, t: str) -> str:
        len_s, len_t = len(s), len(t)

        if len_s < len_t:
            return ''

        count = Counter(t)
        left = right = 0
        remains = len_t
        res = ''

        if s[right] in count:
            count[s[right]] -= 1
            if count[s[right]] >= 0:
                remains -= 1

        while left <= len_s - len_t and right <= len_s:
            if remains > 0:
                right += 1
                if right < len_s and s[right] in count:
                    count[s[right]] -= 1
                    if count[s[right]] >= 0:
                        remains -= 1
            elif remains == 0:
                if not res or right - left + 1 < len(res):
                    res = s[left:right + 1]
                if s[left] in count:
                    count[s[left]] += 1
                    if count[s[left]] > 0:
                        remains += 1
                left += 1

        return res

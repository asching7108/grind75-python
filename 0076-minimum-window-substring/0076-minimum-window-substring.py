class Solution:
    def minWindow(self, s: str, t: str) -> str:
        len_s, len_t = len(s), len(t)

        if len_s < len_t:
            return ''

        count = Counter(t)
        remains = len_t
        # Initialize two pointers left and right to form a sliding window
        l, r = 0, 0
        ans = ''

        while r < len_s:
            ch = s[r]
            # Update count with the char at the right pointer
            if ch in count:
                count[ch] -= 1
                if count[ch] >= 0:
                    remains -= 1

            # When we have all the chars in t in the sliding window,
            # keep moving the left pointer and update the answer
            while l <= r and remains == 0:
                ch = s[l]
                if ch in count:
                    count[ch] += 1
                    if count[ch] > 0:
                        remains += 1
                if not ans or r - l + 1 < len(ans):
                    ans = s[l : r + 1]
                l += 1

            # Keep moving the right pointer
            r += 1

        return ans

# Time complexity: O(S + T) where S is len(s) and T is len(t)
# Space complexity: O(T) when T has all unique characters
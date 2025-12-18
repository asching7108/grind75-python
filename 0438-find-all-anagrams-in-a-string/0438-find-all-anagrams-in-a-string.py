class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s, len_p = len(s), len(p)
        if len_p > len_s:
            return []

        # Build a haspmap of p's letters and corresponding frequencies
        frequency = {}
        for ch in p:
            if ch in frequency:
                frequency[ch][0] += 1
            else:
                frequency[ch] = [1, 0]

        result = []
        remains = len_p

        # Check if the substring starting from index 0 is an anagram of p
        # and update the frequency map accordingly
        for i in range(len_p):
            if s[i] in frequency:
                frequency[s[i]][1] += 1
                if frequency[s[i]][1] <= frequency[s[i]][0]:
                    remains -= 1
        if remains == 0:
            result.append(0)

        for i in range(1, len_s - len_p + 1):
            if s[i - 1] in frequency:
                frequency[s[i - 1]][1] -= 1
                if frequency[s[i - 1]][1] < frequency[s[i - 1]][0]:
                    remains += 1
            if s[i + len_p - 1] in frequency:
                frequency[s[i + len_p - 1]][1] += 1
                if frequency[s[i + len_p - 1]][1] <= frequency[s[i + len_p - 1]][0]:
                    remains -= 1
            if remains == 0:
                result.append(i)

        return result
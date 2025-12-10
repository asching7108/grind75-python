class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # BFS
        # words = set(wordDict)
        # queue = deque([0])
        # seen = set()

        # while queue:
        #     start = queue.popleft()
        #     if start == len(s):
        #         return True

        #     for end in range(start + 1, len(s) + 1):
        #         if end in seen:
        #             continue

        #         if s[start:end] in words:
        #             queue.append(end)
        #             seen.add(end)

        # return False

        # N is the length of s
        # M is the length of wordDict
        # K is the average length of the words in wordDict
        # Time complexity: O(N^3 + MK), BFS costs up to O(N^3) as handling a node costs O(N^2)
        # as we iterate over nodes in front of the current node for O(N) and for each node end
        # we create a substring also for O(N). We also spent O(MK) to create the set words.
        # Space complexity: O(N + MK), O(N) space for queue and seen, O(MK) for the set words.

        # DP
        @cache
        def dp(i):
            if i < 0:
                return True

            for word in wordDict:
                if s[i - len(word) + 1 : i + 1] == word and dp(i - len(word)):
                    return True

            return False

        return dp(len(s) - 1)

        # N is the length of s
        # M is the length of wordDict
        # K is the average length of the words in wordDict
        # Time complexity: O(NMK) as there are N states of dp(i) and for each state we iterate
        # over M words for which we perform some substring operations which cost O(k)
        # Space complexity: O(N)
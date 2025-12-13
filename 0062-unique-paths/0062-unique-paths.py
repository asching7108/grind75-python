class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.ans = 0

        def backtrack(self, i, j) -> None:
            if i == m - 1 and j == n - 1:
                self.ans += 1
                return

            if i < m - 1:
                backtrack(self, i + 1, j)
            if j < n - 1:
                backtrack(self, i, j + 1)

        backtrack(self, 0, 0)
        return self.ans
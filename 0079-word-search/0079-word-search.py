class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(row, col, path):
            if len(path) == len(word):
                return True

            res = False
            if (0 <= row < m
                and 0 <= col < n
                and (row, col) not in path
                and board[row][col] == word[len(path)]
            ):
                path.append((row, col))
                for y, x in directions:
                    if dfs(row + y, col + x, path):
                        return True
                path.pop()

            return False
            
        for row in range(m):
            for col in range(n):
                if dfs(row, col, []):
                    return True

        return False
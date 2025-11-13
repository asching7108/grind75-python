class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def isValid(row, col):
            return 0 <= row < m and 0 <= col < n

        m, n = len(mat), len(mat[0])
        res = [row[:] for row in mat]
        queue = deque()
        seen = set()

        # Start BFS on all 0s
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    queue.append((row, col, 0))
                    seen.add((row, col))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            row, col, steps = queue.popleft()

            for dx, dy in directions:
                nextRow, nextCol = row + dy, col + dx
                if (nextRow, nextCol) not in seen and isValid(nextRow, nextCol):
                    seen.add((nextRow, nextCol))
                    queue.append((nextRow, nextCol, steps + 1))
                    res[nextRow][nextCol] = steps + 1

        return res

# Time complexity: O(m * n)
# Space complexity: O(m * n)
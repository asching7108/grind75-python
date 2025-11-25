class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        nr, nc = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque()
        res = 0

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))

        while queue:
            row, col, mins = queue.popleft()
            for x, y in directions:
                if (
                    0 <= row + x < nr
                    and 0 <= col + y < nc
                    and grid[row + x][col + y] == 1
                ):
                    grid[row + x][col + y] = 2
                    queue.append((row + x, col + y, mins + 1))
                    res = mins + 1

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 1:
                    return -1

        return res

# Time complexity: O(m * n)
# Space complexity: O(min(m, n))
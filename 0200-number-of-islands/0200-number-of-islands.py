class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        nr, nc = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        res = 0

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    res += 1
                    grid[r][c] = '0'
                    neighbors = deque([(r, c)])
                    while neighbors:
                        row, col = neighbors.popleft()
                        for x, y in directions:
                            if (
                                0 <= row + x < nr
                                and 0 <= col + y < nc
                                and grid[row + x][col + y] == '1'
                            ):
                                grid[row + x][col + y] = '0'
                                neighbors.append((row + x, col + y))

        return res

# Time complexity: O(m * n)
# Space complexity: O(min(m, n))
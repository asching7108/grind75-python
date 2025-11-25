class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        nr, nc = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque()
        minutes_elapsed, fresh_oranges = 0, 0

        for r in range(nr):
            for c in range(nc):
                # Prepare to start multi-source BFS from all rotten oranges
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        while queue:
            row, col, mins = queue.popleft()
            for x, y in directions:
                if (
                    0 <= row + x < nr
                    and 0 <= col + y < nc
                    and grid[row + x][col + y] == 1
                ):
                    grid[row + x][col + y] = 2
                    fresh_oranges -= 1
                    queue.append((row + x, col + y, mins + 1))
                    minutes_elapsed = mins + 1

        return minutes_elapsed if fresh_oranges == 0 else -1

# Time complexity: O(n)
# Space complexity: O(min(m, n))
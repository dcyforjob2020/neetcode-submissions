class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0

        rows = len(grid)
        cols = len(grid[0])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return 0

            if not grid[row][col]:
                return 0

            grid[row][col] = 0

            area = 1

            for add_row, add_col in directions:
                area += dfs(row + add_row, col + add_col)

            return area

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]:
                    res = max(res, dfs(row, col))

        return res
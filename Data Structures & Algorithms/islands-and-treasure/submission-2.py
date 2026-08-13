class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        q = []

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j, 0))

        for r, c, distance in q:
            if r < 0 or r >= rows or c < 0 or c >= cols:
                continue

            val = grid[r][c]

            if val == -1:
                continue

            if (r, c) in visited:
                continue

            visited.add((r, c))

            grid[r][c] = min(distance, val)

            q.append((r - 1, c, distance + 1))
            q.append((r + 1, c, distance + 1))
            q.append((r, c - 1, distance + 1))
            q.append((r, c + 1, distance + 1))
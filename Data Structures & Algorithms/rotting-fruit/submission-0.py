class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        q = []
        total = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    total += 1
                if grid[i][j] == 2:
                    total += 1
                    q.append((i, j, 0))

        visited = set()
        max_distance = 0

        for r, c, distance in q:
            if r < 0 or r >= rows or c < 0 or c >= cols:
                continue

            if (r, c) in visited:
                continue

            if grid[r][c] == 0:
                continue

            visited.add((r, c))

            max_distance = max(distance, max_distance)

            q.append((r - 1, c, distance + 1))
            q.append((r + 1, c, distance + 1))
            q.append((r, c - 1, distance + 1))
            q.append((r, c + 1, distance + 1))

        return max_distance if len(visited) == total else -1
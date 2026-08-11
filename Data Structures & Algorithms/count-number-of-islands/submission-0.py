class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        m = len(grid)
        n = len(grid[0])

        visited = set()

        def dfs(x, y):
            if x >= n or x < 0 or y < 0 or y >= m:
                return

            if (x, y) in visited:
                return
            
            visited.add((x, y))

            if grid[y][x] == "0":
                return

            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        for i in range(m):
            for j in range(n):
                if (j, i) in visited:
                    continue


                if grid[i][j] == "1":
                    res += 1

                    dfs(j, i)
                else:
                    visited.add((j, i))

        return res
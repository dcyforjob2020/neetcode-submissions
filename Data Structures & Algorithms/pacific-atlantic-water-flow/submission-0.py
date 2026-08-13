class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []

        rows = len(heights)
        cols = len(heights[0])

        def bfs(q, visited):
            for r, c, h in q:
                if r < 0 or r >= rows or c < 0 or c >= cols:
                    continue

                if (r, c) in visited:
                    continue

                height = heights[r][c]

                if h > height:
                    continue

                visited.add((r, c))

                q.append((r - 1, c,height))
                q.append((r + 1, c,height))
                q.append((r, c - 1,height))
                q.append((r, c + 1,height))

        pacific_q = []
        pacific_visited = set()

        for i in range(cols):
            pacific_q.append((0, i, heights[0][i]))
        for i in range(rows):
            pacific_q.append((i, 0, heights[i][0]))

        bfs(pacific_q, pacific_visited)

        atlantic_q = []
        atlantic_visited = set()

        for i in range(cols):
            atlantic_q.append((rows - 1, i, heights[rows - 1][i]))
        for i in range(rows):
            atlantic_q.append((i, cols - 1, heights[i][cols - 1]))

        bfs(atlantic_q, atlantic_visited)

        print(pacific_visited)
        print(atlantic_visited)

        for r, c in pacific_visited:
            if (r, c) in atlantic_visited:
                res.append([r, c])

        return res


import sys
sys.setrecursionlimit(10000)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        
        def dfs(r, c):
            val = board[r][c]

            if val == "X" or (r, c) in cur:
                return False

            if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                return True

            cur.add((r, c))
            visited.add((r, c))

            return dfs(r - 1, c) or dfs(r + 1, c) or dfs(r, c - 1) or dfs(r, c + 1)


        rows = len(board)
        cols = len(board[0])

        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if (i, j) in visited or board[i][j] == "X":
                    continue

                cur = set()

                if not dfs(i, j):
                    for r, c in cur:
                        board[r][c] = "X"
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        def dfs(r, c):
            if r < 0 or r > rows - 1 or c < 0 or c > cols - 1 or board[r][c] != "O":
                return

            board[r][c] = "T"

            for row, col in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                dfs(row, col)

        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols - 1)

        for i in range(cols):
            dfs(0, i)
            dfs(rows - 1, i)


        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "T":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"

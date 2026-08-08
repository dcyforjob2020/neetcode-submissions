class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False

        m = len(board)
        n = len(board[0])

        visited = set()

        def dfs(row, col, cur):
            nonlocal res

            if res:
                return
            
            if cur == word:
                res = True
                return

            if len(cur) >= len(word):
                return

            next_row = row
            next_col = col + 1
            right = (next_row, next_col)

            if col < n - 1 and right not in visited:
                visited.add(right)
                dfs(next_row, next_col, cur + board[next_row][next_col])
                visited.remove(right)

            next_row = row
            next_col = col - 1
            left = (next_row, next_col)

            if col > 0 and left not in visited:
                visited.add(left)
                dfs(next_row, next_col, cur + board[next_row][next_col])
                visited.remove(left)

            next_row = row + 1 
            next_col = col
            down = (next_row, next_col)

            if row < m - 1 and down not in visited:
                visited.add(down)
                dfs(next_row, next_col, cur + board[next_row][next_col])
                visited.remove(down)

            next_row = row - 1
            next_col = col
            up = (next_row, next_col)

            if row > 0 and up not in visited:
                visited.add(up)
                dfs(next_row, next_col, cur + board[next_row][next_col])
                visited.remove(up)

        for i in range(m):
            for j in range(n):

                if board[i][j] == word[0]:
                    visited.add((i, j))
                    dfs(i, j, word[0])
                    visited.remove((i, j))

                    if res:
                        return res

        return res
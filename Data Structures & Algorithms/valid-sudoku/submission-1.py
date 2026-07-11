class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]

                if val == ".":
                    continue

                if val in rows[row]:
                    return False
                elif val in cols[col]:
                    return False
                elif val in squares[(row // 3) * 3 + col // 3]:
                    return False

                rows[row].add(val)
                cols[col].add(val)
                squares[(row // 3) * 3 + col // 3].add(val)

        return True
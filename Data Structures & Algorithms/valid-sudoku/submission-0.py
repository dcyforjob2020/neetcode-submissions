class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # create set for each row, col and boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # loop through all elements in the board
        for i in range(9):
            for j in range(9):
                value = board[i][j]

                # if value is ".", skip
                if value == ".":
                    continue

                # get row, col, box set
                row = rows[i]
                col = cols[j]
                box = boxes[i // 3 * 3 + j // 3]
                # if value is in set, then return false
                if value in row or value in col or value in box:
                    return False

                # add to row, col, box set
                row.add(value)
                col.add(value)
                box.add(value)

        # pass all, return True
        return True
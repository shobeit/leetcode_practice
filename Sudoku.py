# You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

# Each row must contain the digits 1-9 without duplicates.
# Each column must contain the digits 1-9 without duplicates.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
# Return true if the Sudoku board is valid, otherwise return false

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        seen = set()

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                
                row = (r, val)
                col = (val, c)
                box = (r // 3, c // 3, val)

                if row in seen or col in seen or box in seen:
                    return False
                
                seen.add(row)
                seen.add(col)
                seen.add(box)

        return True
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # init
        row, col, box = set(), set(), set()
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    box_ind = j // 3 + ((i // 3) * 3)
                    if (i, num) in row or (j, num) in col or (box_ind, num) in box:
                        return False
                    row.add((i, num))
                    col.add((j, num))
                    box.add((box_ind, num))
        return True

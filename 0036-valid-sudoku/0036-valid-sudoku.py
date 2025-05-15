class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    rKey = (board[row][col], "row", row)
                    cKey = (board[row][col], "col", col)
                    bKey = (board[row][col], "box", row // 3, col // 3)

                    if rKey in seen or cKey in seen or bKey in seen:
                        return False

                    seen.add(rKey)
                    seen.add(cKey)
                    seen.add(bKey)
        return True

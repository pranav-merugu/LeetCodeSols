class Solution:
    def checkBox(self, board, row, col) -> bool:
        nums = set()
        for i in range(row, row+3):
            for j in range(col, col+3):
                if board[i][j] != '.':
                    if board[i][j] in nums:
                        return False
                    nums.add(board[i][j])
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            nums = set()
            for col in range(9):
                if board[row][col] != '.':
                    if board[row][col] in nums:
                        return False
                    nums.add(board[row][col])
        
        for col in range(9):
            nums = set()
            for row in range(9):
                if board[row][col] != '.':
                    if board[row][col] in nums:
                        return False
                    nums.add(board[row][col])
            
        for row in range(3):
            for col in range(3):
                if self.checkBox(board, row * 3, col * 3) == False:
                    return False

        return True

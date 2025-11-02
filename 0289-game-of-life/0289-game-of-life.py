class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #2 is a 0 changed to a 1 and 3 is a 1 changed to a 0
        rows, cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
                liveNeighbor = 0
                for dr, dc in directions:
                    if 0 <= row + dr < rows and 0 <= col + dc < cols and (board[row+dr][col+dc] == 1 or board[row+dr][col+dc] == 3):
                        liveNeighbor += 1
                
                if board[row][col] == 1 and liveNeighbor < 2:
                    board[row][col] = 3
                elif board[row][col] == 1 and (liveNeighbor == 2 or liveNeighbor == 3):
                    board[row][col] = 1
                elif board[row][col] == 1 and liveNeighbor > 3:
                    board[row][col] = 3
                elif board[row][col] == 0 and liveNeighbor == 3:
                    board[row][col] = 2
                
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 2:
                    board[row][col] = 1
                elif board[row][col] == 3:
                    board[row][col] = 0
        



                    
                    


        
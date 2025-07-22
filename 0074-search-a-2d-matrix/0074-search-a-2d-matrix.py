class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        leftRows = 0
        rightRows = len(matrix) - 1
        while leftRows <= rightRows:
            mid = (leftRows + rightRows) // 2
            if (target > matrix[mid][0]):
                leftRows = mid + 1
            elif (target < matrix[mid][0]):
                rightRows = mid - 1
            else:
                return True

        row = (leftRows + rightRows) // 2

        leftCol = 0
        rightCol = len(matrix[row]) - 1
        while leftCol <= rightCol:
            mid = (leftCol + rightCol) // 2
            if (target > matrix[row][mid]):
                leftCol = mid + 1
            elif (target < matrix[row][mid]):
                rightCol = mid - 1
            else:
                return True
        
        return False

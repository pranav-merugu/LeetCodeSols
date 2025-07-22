class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        leftRows = 0
        rightRows = rows - 1
        while leftRows < rightRows:
            mid = (leftRows + rightRows) // 2
            if (target > matrix[mid][-1]):
                leftRows = mid + 1
            elif (target < matrix[mid][-1]):
                rightRows = mid
            else:
                return True

        leftCol = 0
        rightCol = len(matrix[0]) - 1
        while leftCol <= rightCol:
            mid = (leftCol + rightCol) // 2
            if (target > matrix[leftRows][mid]):
                leftCol = mid + 1
            elif (target < matrix[leftRows][mid]):
                rightCol = mid - 1
            else:
                return True
        
        return False

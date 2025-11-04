class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        rows, cols = len(matrix), len(matrix[0])

        def outer_loop(srow, scol, erow, ecol):
            for i in range(scol, ecol):
                if not 0 <= i < cols or len(res) >= rows * cols:
                    break
                res.append(matrix[srow][i])
            for i in range(srow + 1, erow):
                if not 0 <= i < rows or len(res) >= rows * cols:
                    break
                res.append(matrix[i][ecol - 1])
            for i in range(ecol - 2, scol - 1, -1):
                if (not 0 <= i < cols) or len(res) >= rows * cols:
                    break
                res.append(matrix[erow - 1][i])
            for i in range(erow - 2, srow, -1):
                if not 0 <= i < rows or len(res) >= rows * cols:
                    break
                res.append(matrix[i][scol])
                
        srow, erow = 0, rows
        scol, ecol = 0, cols
        while srow < erow and scol < ecol:
            outer_loop(srow, scol, erow, ecol)
            srow += 1
            scol += 1
            erow -= 1
            ecol -= 1
        
        return res

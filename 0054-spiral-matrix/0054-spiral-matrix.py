class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

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

        res = []
        srow, erow = 0, len(matrix) - 1
        scol, ecol = 0, len(matrix[0]) - 1
        while srow <= erow and scol <= ecol:
            for i in range(scol, ecol + 1):
                res.append(matrix[srow][i])
            srow += 1

            for i in range(srow, erow + 1):
                res.append(matrix[i][ecol])
            ecol -= 1

            if srow <= erow:
                for i in range(ecol, scol - 1, -1):
                    res.append(matrix[erow][i])
                erow -= 1

            if scol <= ecol:
                for i in range(erow, srow - 1, -1):
                    res.append(matrix[i][scol])
                scol += 1
            
        return res

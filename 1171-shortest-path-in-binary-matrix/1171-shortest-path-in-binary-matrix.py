from collections import deque 

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        if n == 1:
            return 1

        queue = deque([(0, 0, 1)])
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        visited = {(0, 0)}
        while queue:
            r, c, d = queue.popleft()
            if r == n - 1 and c == n - 1:
                return d

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] == 0:
                    queue.append((nr, nc, d + 1))
                    visited.add((nr, nc))
        
        return -1
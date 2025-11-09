from collections import deque 

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        if n == 1:
            return 1

        queue = deque()
        queue.append((0, 0, 1))
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        minLength = float('inf')
        visited = set()
        visited.add((0, 0))
        while queue:
            cur = queue.popleft()

            for dl, dr in directions:
                if 0 <= cur[0] + dl < n and 0 <= cur[1] + dr < n and (cur[0] + dl, cur[1] + dr) not in visited and grid[cur[0] + dl][cur[1] + dr] == 0:
                    if cur[0] + dl == n - 1 and cur[1] + dr == n - 1:
                        minLength = min(minLength, cur[2] + 1)
                    queue.append((cur[0] + dl, cur[1] + dr, cur[2] + 1))
                    visited.add((cur[0] + dl, cur[1] + dr))
        
        if minLength == float('inf'):
            return -1
        else:
            return minLength
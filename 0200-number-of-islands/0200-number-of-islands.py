from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #assumption we don't need to preserve original grid values

        def bfs(grid, cur):
            w, l = len(grid), len(grid[0])
            q = deque()
            q.append(cur)
            while q:
                point = q.popleft()
                if (point[0] - 1) >= 0 and grid[point[0] - 1][point[1]] == "1":
                    grid[point[0] - 1][point[1]] = "0"
                    q.append((point[0] - 1, point[1]))
                if (point[0] + 1) < w and grid[point[0] + 1][point[1]] == "1":
                    grid[point[0] + 1][point[1]] = "0"
                    q.append((point[0] + 1, point[1]))
                if (point[1] - 1) >= 0 and grid[point[0]][point[1] - 1] == "1":
                    grid[point[0]][point[1] - 1] = "0"
                    q.append((point[0], point[1] - 1))
                if (point[1] + 1) < l and grid[point[0]][point[1] + 1] == "1":
                    grid[point[0]][point[1] + 1] = "0"
                    q.append((point[0], point[1] + 1))

            return grid
        
        num_islands = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    grid = bfs(grid, (x, y))
                    num_islands += 1
        
        return num_islands



from collections import deque
from collections import defaultdict

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if grid == [[0]] or grid == [[0,0,0,0]]:
            return 0

        adjacency = defaultdict(list)
        rotten = deque()
        numOranges = 0
        rows, cols = len(grid), len(grid[0])

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] != 0:
                    numOranges += 1

                    if grid[row][col] == 2:
                        rotten.append((row, col))
                    
                    for dr, dc in directions:
                        if (0 <= row + dr < rows) and (0 <= col + dc < cols) and grid[row][col] != 0:
                            adjacency[(row, col)].append((row+dr, col+dc))
        
        visited = set()
        numLevels = 0
        levelSize = len(rotten)
        while rotten:
            for i in range(levelSize):
                cur = rotten.popleft()
                visited.add(cur)
                for row, col in adjacency[cur]:
                    if (row, col) not in visited:
                        if grid[row][col] == 1:
                            grid[row][col] = 2
                            rotten.append((row, col))
            numLevels += 1
            levelSize = len(rotten)
        
        if len(visited) == numOranges:
            return numLevels - 1
        else:
            return -1
        




                    
                    

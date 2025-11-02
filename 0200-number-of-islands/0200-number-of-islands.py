from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        num_islands = 0

        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] = "0"  # Mark as visited immediately
            
            # Direction vectors: up, down, left, right
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
            while queue:
                row, col = queue.popleft()
                
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    
                    # Check bounds and if it's land
                    if (0 <= new_row < rows and 
                        0 <= new_col < cols and 
                        grid[new_row][new_col] == "1"):
                        
                        grid[new_row][new_col] = "0"  # Mark visited
                        queue.append((new_row, new_col))
        
        #scan for islands
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    num_islands += 1
        
        return num_islands



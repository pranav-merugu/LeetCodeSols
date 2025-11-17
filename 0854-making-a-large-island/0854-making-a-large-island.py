from collections import deque

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        island_id = 2                     # Start at 2 so 0 and 1 are not confused
        area = {}                         # island_id -> island_area

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # BFS to label and compute island area
        def bfs(r, c, id):
            q = deque([(r, c)])
            grid[r][c] = id
            size = 1

            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = id
                        size += 1
                        q.append((nx, ny))

            return size

        # 1st pass - label islands and store areas
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area[island_id] = bfs(r, c, island_id)
                    island_id += 1

        # If no zero exists → whole grid is land
        if len(area) == 0:
            return 1

        max_area = max(area.values(), default=0)

        # 2nd pass - check every zero
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    neighbor_ids = set()
                    for dx, dy in directions:
                        nr, nc = r + dx, c + dy
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > 1:
                            neighbor_ids.add(grid[nr][nc])

                    # connect all neighbor islands + this flipped cell
                    new_area = 1 + sum(area[id] for id in neighbor_ids)
                    max_area = max(max_area, new_area)

        return max_area

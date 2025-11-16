class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(coord, visited):
            row = coord[0]
            col = coord[1]
            for dr, dc in directions:
                if 0 <= row + dr < m and 0 <= col + dc < n and (row + dr, col + dc) not in visited and heights[row][col] <= heights[row + dr][col + dc]:
                    visited.add((row + dr, col + dc))
                    bfs((row + dr, col + dc), visited)
        
        for i in range(n):
            pacific.add((0, i))
            bfs((0, i), pacific)
            atlantic.add((m-1, i))
            bfs((m - 1, i), atlantic)

        for i in range(m):
            pacific.add((i, 0))
            bfs((i, 0), pacific)
            atlantic.add((i, n - 1))
            bfs((i, n - 1), atlantic)

        
        return list(pacific.intersection(atlantic))

        
from collections import defaultdict

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return []

        inf = 2**31 - 1
        rows, cols = len(rooms), len(rooms[0])
        gates = []
        for row in range(rows):
            for col in range(cols):
                if rooms[row][col] == 0:
                    gates.append((row, col, 0))

        q = deque()
        q.extend(gates)
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]


        while q:
            row, col, dist = q.popleft()
            for dr, dc in directions:
                if 0 <= row + dr < rows and 0 <= col + dc < cols and rooms[row + dr][col + dc] == inf:
                    rooms[row + dr][col + dc] = dist + 1
                    q.append((row + dr, col + dc, dist + 1))


        
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-n for n in stones]
        heapq.heapify(h)

        while len(h) >= 2:
            stone1 = -heapq.heappop(h)
            stone2 = -heapq.heappop(h)
            if stone1 != stone2:
                heapq.heappush(h, -(stone1 - stone2))
        
        if len(h) == 0:
            return 0
        else:
            return -h[0]


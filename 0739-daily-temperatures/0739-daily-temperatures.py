from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = deque([])
        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                prevIdx, prevTemp = stack.pop()
                res[prevIdx] = idx - prevIdx
            stack.append((idx, temp))
        
        return res

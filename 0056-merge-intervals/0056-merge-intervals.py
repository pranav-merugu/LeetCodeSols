from heapq import heapify, heappush, heappop

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0]) #sort all intervals by their first element since we want to merge from 0 -> greatest start
        result = []

        for start, end in intervals:
            if len(result) == 0 or result[-1][1] < start: #if it does not overlap or there's no previous interal, just add the current interval
                result.append([start, end])
            else: #if it does overlap, merge the two
                result[-1][1] = max(result[-1][1], end)
        return result



        
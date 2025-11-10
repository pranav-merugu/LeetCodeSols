class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [[intervals[0][0], intervals[0][1]]]
        for start, end in intervals[1:]:
            if res[-1][0] <= start <= res[-1][1]:
                res[-1][1] = max(end, res[-1][1])
            else:
                res.append([start, end])
    
        return res

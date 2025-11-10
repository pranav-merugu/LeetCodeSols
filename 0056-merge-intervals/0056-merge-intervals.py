class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for start, end in intervals:
            if not res:
                res.append([start, end])
            else:
                if res[-1][0] <= start <= res[-1][1]:
                    res[-1][1] = max(end, res[-1][1])
                else:
                    res.append([start, end])
        
        return res

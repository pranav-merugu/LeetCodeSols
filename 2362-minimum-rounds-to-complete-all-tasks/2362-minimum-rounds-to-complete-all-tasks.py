from collections import defaultdict

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = defaultdict(int)
        for task in tasks:
            freq[task] += 1
        
        res = 0
        for count in freq.values():
            if count == 1:
                return -1
            
            if count % 3 == 0:
                res += count // 3
            else:
                res += count // 3 + 1
        
        return res
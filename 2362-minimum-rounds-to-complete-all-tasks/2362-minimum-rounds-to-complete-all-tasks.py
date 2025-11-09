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
            while count > 0:
                if count == 2 or count == 4:
                    count -= 2
                else:
                    count -= 3
                res += 1
        
        return res
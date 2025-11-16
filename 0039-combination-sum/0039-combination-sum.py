from collections import defaultdict

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(i, s):
            if s == 0:
                res.append(cur[:])
                return 
            
            if candidates[i] > s:
                return
            
            for idx in range(i, len(candidates)):
                cur.append(candidates[idx])
                dfs(idx, s - candidates[idx])
                cur.pop()
        
        candidates.sort()

        cur = []
        res = []
        dfs(0, target)

        return res
        
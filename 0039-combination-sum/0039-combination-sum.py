from collections import defaultdict

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(idx, sum):
            if sum == target:
                result.append(cur[:])
                return
            
            if sum > target:
                return
            
            for i in range(idx, len(candidates)):
                cur.append(candidates[i])
                backtrack(i, sum + candidates[i])
                cur.pop()
            
        
        cur = []
        backtrack(0, 0)

        return result
            

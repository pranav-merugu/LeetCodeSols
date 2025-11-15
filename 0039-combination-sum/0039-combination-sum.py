from collections import defaultdict

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = defaultdict(set)

        for c in candidates:
            if c <= target:
                dp[c].add((c,))

        for i in range(1, target + 1):
            if len(dp[i]) > 0:
                for c in candidates:
                    if c + i <= target:
                        for sol in dp[i]:
                            dp[c+i].add(sol + (c,))
        
        res = set()
        for sol in dp[target]:
            res.add(tuple(sorted(sol)))
        return list(res)
        
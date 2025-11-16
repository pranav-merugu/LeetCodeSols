class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        if n == 1:
            return True

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(n):
            if dp[i] == True:
                for j in range(i, i + nums[i] + 1):
                    if j == n - 1:
                        return True
                    elif j < n - 1:
                        dp[j] = True
        
        return False
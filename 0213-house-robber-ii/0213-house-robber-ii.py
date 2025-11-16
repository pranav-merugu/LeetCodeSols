class Solution:
    def rob(self, nums: List[int]) -> int:

        def houseRob(houses):
            n = len(houses)

            dp = [0] * (n + 1)
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            for i in range(2, n):
                dp[i] = max(houses[i] + dp[i - 2], dp[i - 1])
            
            return dp[n - 1]
        
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)

        first = houseRob(nums[:-1])
        second = houseRob(nums[1:])

        return max(first, second)        


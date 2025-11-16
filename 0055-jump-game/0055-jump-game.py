class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0

        for pos, reach in enumerate(nums):
            if pos > maxReach:
                return False
            
            maxReach = max(maxReach, pos + reach)

            if maxReach >= len(nums) - 1:
                return True
        
        return False
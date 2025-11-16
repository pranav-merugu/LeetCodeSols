from collections import defaultdict, deque

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max_length = 0
        dp = {}

        for num in nums:
            if num not in numSet:
                continue

            cur = num
            while cur in numSet:
                numSet.remove(cur)
                cur += 1

            dp[num] = dp.get(cur, 0) + (cur - num)
            max_length = max(max_length, dp[num])
        
        return max_length

            

            
        
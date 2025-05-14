class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            output.append(prefix)
            prefix *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        
        return output
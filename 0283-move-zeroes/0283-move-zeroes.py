class Solution(object):
    def moveZeroes(self, nums):
        nonzero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nonzero], nums[i] = nums[i], nums[nonzero]
                nonzero += 1
            


        
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            i = abs(num) - 1
            nums[i] = -1 * abs(nums[i])
        result = []
        for i in range(len(nums)):
            if (nums[i] > 0):
                result.append(i+1)
        return result

        #[4,3,2,7,8,2,3,1]
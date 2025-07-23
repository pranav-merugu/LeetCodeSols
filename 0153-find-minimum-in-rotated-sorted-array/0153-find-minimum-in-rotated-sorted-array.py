class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1 #
        minNum = nums[left] #3
        while left <= right:
            if nums[left] < nums[right]:
                minNum = min(minNum, nums[left])
                break

            mid = (left + right) // 2 #4
            minNum = min(minNum, nums[mid])
            if (nums[left] <= nums[mid]): # 0 < 2
                left = mid + 1 #4
            else:
                right = mid - 1 #4
        return minNum

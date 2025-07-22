class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 #0
        right = len(nums) #6
        while left < right:
            mid = (left + right) // 2 #3
            if (target > nums[mid]): #nums[mid] = 5
                left = mid + 1
            elif (target < nums[mid]):
                right = mid  #3
            else:
                return mid
        return -1
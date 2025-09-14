from heapq import heapify, heappop, heappush

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        end = m + n - 1 #we want to add elements from the end to the front

        while m > 0 and n > 0: #iterate until you run out of elements in one of the lists
            if nums1[m - 1] > nums2[n - 1]: #find the greater element from the two lists and add to end
                nums1[end] = nums1[m-1]
                m -= 1
            else:
                nums1[end] = nums2[n-1]
                n -= 1
            end -= 1
        
        while n > 0: #edge case, if there's numbers in nums2 that are smaller than the smallest element in nums1, then the loop above won't add them, so we do it here manually
            nums1[end] = nums2[n-1]
            n -= 1
            end -= 1

        return nums1
                



        
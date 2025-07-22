class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        maxSize = piles[-1]
        left = 1
        right = maxSize #30
        while left <= right:
            k = (left + right) // 2 #15
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            if (hours > h):
                left = k + 1
            else:
                right = k - 1
        
        return left
            



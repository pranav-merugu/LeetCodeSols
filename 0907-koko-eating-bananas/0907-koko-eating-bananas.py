class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxSize = max(piles)
        left = 1
        right = maxSize #30
        minRate = right
        while left <= right:
            k = (left + right) // 2 #15
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            if (hours > h):
                left = k + 1
            else:
                minRate = min(minRate, k)
                right = k - 1
        
        return minRate
            



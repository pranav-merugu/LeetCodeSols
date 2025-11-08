from bisect import bisect_left

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        m = len(heaters)
        heaters.sort()
        maxDist = -1
        for house in houses:
            nearestHeat = 0
            checkIdx = bisect_left(heaters, house)
            if checkIdx == 0:
                nearestHeat = heaters[0] - house
            elif checkIdx == m:
                nearestHeat = house - heaters[-1]
            else:
                nearestHeat = min(house - heaters[checkIdx - 1], heaters[checkIdx] - house)
            maxDist = max(nearestHeat, maxDist)
        return maxDist

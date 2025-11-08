from bisect import bisect_left, bisect_right

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        m = len(heaters)
        heaters.sort()
        minDistances = []
        for house in houses:
            minD = float('inf')
            checkIdx = bisect_left(heaters, house)
            if 0 <= checkIdx < m:
                if abs(house - heaters[checkIdx]) < minD:
                    minD = abs(house - heaters[checkIdx])
            if 0 <= checkIdx - 1 < m:
                if abs(house - heaters[checkIdx - 1]) < minD:
                    minD = abs(house - heaters[checkIdx - 1])
            minDistances.append(minD)
        return max(minDistances)

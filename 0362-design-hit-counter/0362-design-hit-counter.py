class HitCounter:

    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        lb = max(0, timestamp - 300)
        r = bisect.bisect_right(self.hits, timestamp)
        l = bisect.bisect_right(self.hits, lb)
        return r - l


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
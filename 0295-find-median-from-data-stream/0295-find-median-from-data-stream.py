import heapq


class MedianFinder:

    def __init__(self):
        self.lower = [] # Max heap
        self.upper = [] # Min heap

    def addNum(self, num: int) -> None:
        # Push new value to the lower half first
        heapq.heappush(self.lower, -num)
        # Move one item to the upper half to ensure items are sorted
        heapq.heappush(self.upper, -heapq.heappop(self.lower))

        # Rearrange
        if len(self.lower) < len(self.upper):
            heapq.heappush(self.lower, -heapq.heappop(self.upper))

    # Time complexity: O(log N)

    def findMedian(self) -> float:
        if len(self.lower) > len(self.upper):
            return -self.lower[0]
        return (-self.lower[0] + self.upper[0]) / 2

    # Time complexity: O(1)

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
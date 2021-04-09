import heapq


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lo = []
        self.hi = []
        self.count = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype -> None
        """
        self.count += 1
        heapq.heappush(self.lo, num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.lo) < len(self.hi):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self):
        """
        :rtype -> float
        """
        if self.count % 2 == 1:
            return self.lo[0]
        return (self.lo[0] - self.hi[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
obj.addNum(6)
print(obj.findMedian())
obj.addNum(10)
print(obj.findMedian())
obj.addNum(2)
print(obj.findMedian())
obj.addNum(6)
print(obj.findMedian())
obj.addNum(5)

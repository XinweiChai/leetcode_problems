class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []
        self.odd = False
        self.mid = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.odd = not self.odd

        def positioning(val, left, right):
            if left == right:
                return left
            mid = (left + right) // 2
            if val <= self.l[mid]:
                return positioning(val, left, mid)
            else:
                return positioning(val, mid + 1, right)

        self.l.insert(positioning(num, 0, len(self.l)), num)


    def findMedian(self):
        """
        :rtype: float
        """
        if self.odd:
            return self.l[len(self.l)//2]
        else:
            return (self.l[len(self.l)//2]+self.l[len(self.l)//2-1])/2
# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
obj.addNum(6)
obj.addNum(10)
print(obj.findMedian())
obj.addNum(2)
print(obj.findMedian())
obj.addNum(6)
print(obj.findMedian())
obj.addNum(5)

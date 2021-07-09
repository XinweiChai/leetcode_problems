import bisect
import heapq
from typing import List


class DisjointSet:
    def __init__(self):
        self.v = {}
        self.grp_max = {}

    def make_set(self, x):
        if x not in self.v:
            self.v[x] = x
            self.grp_max[x] = x
            if x - 1 in self.v:
                self.join(x - 1, x)
            if x + 1 in self.v:
                self.join(x, x + 1)

    def find(self, i):
        if i != self.v[i]:
            self.v[i] = self.find(self.v[i])
        return self.v[i]

    def join(self, i, j):
        ri = self.find(i)
        rj = self.find(j)
        self.grp_max[ri] = self.grp_max[rj]
        self.grp_max.pop(j)
        if ri != rj:
            self.v[rj] = ri


# Using disjoint-set
class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ds = DisjointSet()

    def addNum(self, val: int) -> None:
        self.ds.make_set(val)

    def getIntervals(self) -> List[List[int]]:
        return sorted(self.ds.grp_max.items())


# Using bisect
class SummaryRanges2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = set()
        self.intervals = []

    def addNum(self, val: int) -> None:
        if val not in self.nums:
            self.nums.add(val)
            index = bisect.bisect(self.intervals, [val, val])
            if val + 1 not in self.nums and val - 1 not in self.nums:
                self.intervals.insert(index, [val, val])
            elif index == 0:
                self.compare_right_interval(val, index)
            else:
                left_interval = self.intervals[index - 1]
                if val == left_interval[1] + 1:
                    self.intervals[index - 1][1] = val
                    # compare with the next interval: self.interval[index]
                    if index == len(self.intervals) or self.intervals[index][0] > val + 1:
                        return
                    self.intervals[index - 1][1] = self.intervals[index][1]
                    self.intervals.pop(index)
                else:  # val > left_interval[1] + 1
                    # bisect.bisect()的特点，val<下一个interval[0]
                    self.compare_right_interval(val, index)

    def compare_right_interval(self, val, index):
        # compare and merge (if possible) with next/right interval
        # bisect.bisect()的特点，val < 下一个interval[0]
        if index == len(self.intervals):  # 后面没有interval了
            self.intervals.append([val, val])
        elif val + 1 == self.intervals[index][0]:
            self.intervals[index][0] = val
        else:
            self.intervals.insert(index, [val, val])

    def getIntervals(self) -> List[List[int]]:
        return self.intervals


# Using heap
class SummaryRanges3:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []
        self.seen = set()

    def addNum(self, val: int) -> None:
        if val not in self.seen:
            self.seen.add(val)
            heapq.heappush(self.intervals, [val, val])

    def getIntervals(self) -> List[List[int]]:
        tmp = []

        while self.intervals:
            cur = heapq.heappop(self.intervals)
            if tmp and cur[0] <= tmp[-1][1] + 1:
                tmp[-1][1] = max(tmp[-1][1], cur[1])
            else:
                tmp.append(cur)

        self.intervals = tmp
        return self.intervals


if __name__ == '__main__':
    # Your SummaryRanges object will be instantiated and called as such:
    # obj = SummaryRanges()
    # obj.addNum(val)
    # param_2 = obj.getIntervals()
    obj = SummaryRanges3()
    operators = ["addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals",
                 "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals",
                 "addNum", "getIntervals", "addNum", "getIntervals"]
    operands = [[6], [], [6], [], [0], [], [4], [], [8], [], [7], [], [6], [], [4], [], [7], [], [5], []]
    for i, j in zip(operators, operands):
        print(eval('obj.' + i)(*j))

from typing import Sequence
import bisect


class Solution:
    def findRightInterval(self, intervals: Sequence[Sequence[int]]) -> Sequence[int]:
        # sorted_intervals = sorted(enumerate(intervals), key=lambda x: x[1][0])
        l = sorted((e[0], i) for i, e in enumerate(intervals))
        res = []
        for i in intervals:
            temp = bisect.bisect(l, (i[1], -1))
            if temp == len(intervals):
                res.append(-1)
            else:
                res.append(l[temp][1])
        return res


if __name__ == '__main__':
    print(Solution().findRightInterval(intervals=[[3,4],[2,3],[1,2]]))

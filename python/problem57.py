from typing import Sequence


class Solution:
    def insert(self, intervals: Sequence[Sequence[int]], newInterval: Sequence[int]) -> Sequence[Sequence[int]]:
        s, e = newInterval
        left = [i for i in intervals if i[1] < s]
        right = [i for i in intervals if i[0] > e]
        if left + right != intervals:
            s = min(s, intervals[len(left)][0])
            e = max(e, intervals[~len(right)][1])
        return left + [[s, e]] + right


print(Solution().insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]))
# print(Solution().insert(intervals=[[1, 5]], newInterval=[2, 3]))
# print(Solution().insert(intervals=[], newInterval=[5, 7]))

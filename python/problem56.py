from typing import Sequence


class Solution:
    def merge(self, intervals: Sequence[Sequence[int]]) -> Sequence[Sequence[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        merged = [intervals[0]]
        for i in intervals[1:]:
            if i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged.append(i)
        return merged


print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))

class Solution:
    # Which interval would be the best first (leftmost) interval to keep?
    # One that ends first, as it leaves the most room for the rest.
    # So take one with smallest end, remove all the bad ones overlapping it.
    def eraseOverlapIntervals(self, intervals):
        end = float('-inf')
        erased = 0
        intervals.sort(key=lambda x: x[1])
        for i in intervals:
            if i[0] >= end:
                end = i[-1]
            else:
                erased += 1
        return erased


if __name__ == '__main__':
    print(Solution().eraseOverlapIntervals(intervals=[[1, 2], [2, 3], [3, 4], [1, 3]]))

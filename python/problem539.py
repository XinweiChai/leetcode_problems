from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time_set = set(timePoints)
        if len(time_set) < len(timePoints):
            return 0
        timePoints = sorted([int(time[:2]) * 60 + int(time[3:]) for time in time_set])
        timePoints.append(timePoints[0] + 1440)
        return min(timePoints[i + 1] - timePoints[i] for i in range(len(timePoints) - 1))


if __name__ == '__main__':
    print(Solution().findMinDifference(timePoints=["23:59", "00:00"]))

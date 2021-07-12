from functools import lru_cache
from typing import List


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])

        @lru_cache
        def schedule(i, time):
            if i == len(courses):
                return 0
            taken = 0
            if time + courses[i][0] <= courses[i][1]:
                taken = 1 + schedule(i + 1, time + courses[i][0])
            not_taken = schedule(i + 1, time)
            return max(taken, not_taken)

        return schedule(0, 0)


if __name__ == '__main__':
    print(Solution().scheduleCourse(courses=[[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]))

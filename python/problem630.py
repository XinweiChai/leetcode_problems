from functools import lru_cache
from typing import Sequence
import heapq


class Solution:
    # Recursive approach
    def scheduleCourse(self, courses: Sequence[Sequence[int]]) -> int:
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

    # Iterative approach with optimizations in searching the taken course with longest duration
    def scheduleCourse2(self, courses: Sequence[Sequence[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        time = 0
        cnt = 0
        for i in range(len(courses)):
            if time + courses[i][0] <= courses[i][1]:
                time += courses[i][0]
                courses[cnt] = courses[i]
                cnt += 1
            else:
                max_i = i
                for j in range(cnt):
                    if courses[j][0] > courses[max_i][0]:
                        max_i = j
                if courses[max_i][0] > courses[i][0]:
                    time += courses[i][0] - courses[max_i][0]
                    courses[max_i] = courses[i]
        return cnt

    # Using priority queue / heap to store the taken courses
    # If the current course cannot be taken,
    # Try to replace the course with the longest duration with the current course
    def scheduleCourse3(self, courses: Sequence[Sequence[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        time = 0
        taken = []
        for duration, deadline in courses:
            if time + duration <= deadline:
                heapq.heappush(taken, -duration)
                time += duration
            else:
                if taken and duration < -taken[0]:
                    time += heapq.heappop(taken) + duration
                    heapq.heappush(taken, -duration)
        return len(taken)


if __name__ == '__main__':
    print(Solution().scheduleCourse2(courses=[[5, 5], [4, 6], [2, 6]]))

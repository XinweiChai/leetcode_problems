from typing import List
import heapq


class Solution:
    # My solution, using 2 heaps
    def findMaximizedCapital3(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w >= max(capital):
            return w + sum(heapq.nlargest(k, profits))
        candidates = []
        available = []
        projects = sorted(zip(profits, capital))
        for _ in range(k):
            if available:
                w += -heapq.heappop(available)[0]
            else:
                while projects and projects[-1][1] > w:
                    heapq.heappush(candidates, (projects[-1][1], -projects[-1][0]))
                    projects.pop()
                if projects:
                    w += projects.pop()[0]
                else:
                    return w
            while candidates and candidates[0][0] <= w:
                tmpj, tmpi = heapq.heappop(candidates)
                heapq.heappush(available, (tmpi, tmpj))
        return w

    # A more clever solution using one heap
    def findMaximizedCapital2(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w >= max(capital):
            return w + sum(heapq.nlargest(k, profits))
        projects = sorted(zip(capital, profits), reverse=True)
        available = []
        while k > 0:
            while projects and projects[-1][0] <= w:
                heapq.heappush(available, -projects.pop()[1])
            if available:
                w -= heapq.heappop(available)
            else:
                break
            k -= 1
        return w


if __name__ == '__main__':
    print(Solution().findMaximizedCapital2(2, 0, [1, 2, 3], [0, 1, 1]))

from typing import List


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        graph = [[] for _ in range(numCourses)]
        rev_graph = [[] for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
            rev_graph[y].append(x)

        visit = []
        cand = [i for i in range(len(graph)) if not graph[i]]
        while cand:
            cur = cand.pop()
            for i in rev_graph[cur]:
                graph[i].remove(cur)
                if not graph[i]:
                    cand.append(i)
            visit.append(cur)
        if len(visit) != numCourses:
            return []
        return visit


print(Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
print(Solution().findOrder(4, [[1, 0], [0, 1], [3, 1], [3, 2]]))

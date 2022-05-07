from typing import Sequence
from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: Sequence[Sequence[int]]) -> Sequence[int]:
        # graph = [[] for _ in range(numCourses)]
        # rev_graph = [[] for _ in range(numCourses)]
        # for x, y in prerequisites:
        #     graph[x].append(y)
        #     rev_graph[y].append(x)
        #
        # visit = []
        # cand = [i for i in range(len(graph)) if not graph[i]]
        # while cand:
        #     cur = cand.pop()
        #     for i in rev_graph[cur]:
        #         graph[i].remove(cur)
        #         if not graph[i]:
        #             cand.append(i)
        #     visit.append(cur)
        # if len(visit) != numCourses:
        #     return []
        # return visit

        # Kahn's algorithm
        graph = defaultdict(set)
        s = []
        in_degree = [0] * numCourses
        for i in prerequisites:
            # graph[i[1]] = graph.get(i[1], set()) | {i[0]}
            graph[i[1]].add(i[0])
            in_degree[i[0]] += 1
        start = [i for i in range(len(in_degree)) if in_degree[i] == 0]
        while start:
            n = start.pop()
            s.append(n)
            if n in graph:
                for i in graph[n]:
                    in_degree[i] -= 1
                    if in_degree[i] == 0:
                        start.append(i)
                graph.pop(n)
        if graph:
            return []
        else:
            return s

if __name__ == '__main__':
    print(Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
    print(Solution().findOrder(4, [[1, 0], [0, 1], [3, 1], [3, 2]]))

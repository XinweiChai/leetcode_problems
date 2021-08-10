from functools import lru_cache


class Solution:
    # DFS
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)

        # 0 for unvisited, 1 for visited, -1 for visiting
        @lru_cache
        def can_finish_one(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for j in graph[i]:
                if not can_finish_one(j):
                    return False
            visit[i] = 1
            return True

        return all(can_finish_one(i) for i in range(numCourses))
        # for i in range(numCourses):
        #     if not can_finish_one(i):
        #         return False
        # return True

    # BFS, Kahn's algorithm
    def canFinish2(self, numCourses: int, prerequisites) -> bool:
        graph = {}
        in_degree = [0] * numCourses
        for i in prerequisites:
            graph[i[0]] = graph.get(i[0], set()) | {i[1]}
            in_degree[i[1]] += 1
        start = [i for i in range(len(in_degree)) if in_degree[i] == 0]
        while start:
            n = start.pop()
            if n in graph:
                for i in graph[n]:
                    in_degree[i] -= 1
                    if in_degree[i] == 0:
                        start.append(i)
                graph.pop(n)
        return not graph

    # Alternative of solution2
    def canFinish3(self, numCourses: int, prerequisites) -> bool:
        graph = {i: set() for i in range(numCourses)}
        graph_rev = {i: set() for i in range(numCourses)}
        for i in prerequisites:
            graph[i[0]].add(i[1])
            graph_rev[i[1]].add(i[0])
        S = [i for i in graph_rev if not graph_rev[i]]
        while S:
            node = S.pop()
            for m in graph[node]:
                graph_rev[m].remove(node)
                if not graph_rev[m]:
                    S.append(m)
            graph.pop(node)
        return not graph


if __name__ == '__main__':
    print(Solution().canFinish(3, [[0, 1], [0, 2], [1, 2]]))
    # print(Solution().canFinish3(2, [[1, 0]]))
    # print(Solution().canFinish(1, []))
    # print(Solution().canFinish3(5, [[1, 4], [2, 4], [3, 1], [3, 2]]))

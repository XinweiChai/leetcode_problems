class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        # DFS
        # graph = [[] for _ in range(numCourses)]
        # visit = [0 for _ in range(numCourses)]
        # for x, y in prerequisites:
        #     graph[x].append(y)
        #
        # def dfs(i):
        #     if visit[i] == -1:
        #         return False
        #     if visit[i] == 1:
        #         return True
        #     visit[i] = -1
        #     for j in graph[i]:
        #         if not dfs(j):
        #             return False
        #     visit[i] = 1
        #     return True
        #
        # for i in range(numCourses):
        #     if not dfs(i):
        #         return False
        # return True

        # BFS, Kahn's algorithm
        graph = {}
        in_degree = [0] * numCourses
        for i in prerequisites:
            graph[i[0]] = graph[i[0]] | {i[1]} if i[0] in graph else {i[1]}
            in_degree[i[1]] += 1
        start = [i for i in range(len(in_degree)) if in_degree[i] == 0]
        while start:
            n = start.pop()
            if n in graph:
                for i in list(graph[n]):
                    graph[n].remove(i)
                    if not graph[n]:
                        graph.pop(n)
                    in_degree[i] -= 1
                    if in_degree[i] == 0:
                        start.append(i)
        return not graph


print(Solution().canFinish(3, [[0, 1], [0, 2], [2, 0]]))
print(Solution().canFinish(2, [[1, 0]]))
print(Solution().canFinish(1, []))
print(Solution().canFinish(5, [[1, 4], [2, 4], [3, 1], [3, 2]]))

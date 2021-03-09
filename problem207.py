class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        edges_dict = {}
        for i in range(numCourses):
            edges_dict[i] = []
        for i in prerequisites:
            if i[0] in edges_dict:
                edges_dict[i[0]].append(i[1])
        for i in range(numCourses):
            visited = set()
            todo = [i]
            while todo:
                temp = []
                for j in todo:
                    if j in visited:
                        return False
                    visited.add(j)
                    temp += edges_dict[j]
                    edges_dict[j] = []
                todo = temp
        return True


print(Solution().canFinish(3, [[0, 1], [0, 2], [1, 2]]))
# print(Solution().canFinish(2, [[1, 0]]))

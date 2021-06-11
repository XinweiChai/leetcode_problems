from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ds = DisjointSet(len(edges))
        for i in edges:
            if not ds.join(i[0], i[1]):
                return i


class DisjointSet:
    def __init__(self, n):
        self.v = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, i):
        if i != self.v[i]:
            self.v[i] = self.find(self.v[i])
        return self.v[i]

    def join(self, i, j):
        i = self.find(i)
        j = self.find(j)
        if i == j:
            return False
        if self.rank[i] < self.rank[j]:
            i, j = j, i
        self.v[j] = i
        if self.rank[i] == self.rank[j]:
            self.rank[i] += 1
        return True


if __name__ == '__main__':
    print(Solution().findRedundantConnection([[1, 4], [3, 4], [1, 3], [1, 2], [4, 5]]))

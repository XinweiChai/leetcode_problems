from typing import Sequence


class Solution:
    def numSimilarGroups(self, strs: Sequence[str]) -> int:
        def similar(a, b):
            cnt = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    cnt += 1
                    if cnt > 2:
                        return False
            return True

        ds = DisjointSet(len(strs))
        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                if similar(strs[i], strs[j]):
                    ds.join(i, j)
        return ds.size


class DisjointSet:
    def __init__(self, n):
        self.v = [i for i in range(n)]
        self.size = n

    def find(self, i):
        if i != self.v[i]:
            self.v[i] = self.find(self.v[i])
        return self.v[i]

    def join(self, i, j):
        ri = self.find(i)
        rj = self.find(j)
        if ri != rj:
            self.v[rj] = ri
            self.size -= 1

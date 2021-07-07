from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        dct_edge = [set() for _ in range(n)]
        for i, j in edges:
            dct_edge[i].add(j)
            dct_edge[j].add(i)
        leaves = [i for i in range(n) if len(dct_edge[i]) == 1]
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for i in leaves:
                neighbor = dct_edge[i].pop()
                dct_edge[neighbor].remove(i)
                if len(dct_edge[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves


if __name__ == '__main__':
    print(Solution().findMinHeightTrees(n=7, edges=[[0, 1], [1, 2], [1, 3], [2, 4], [3, 5], [4, 6]]))

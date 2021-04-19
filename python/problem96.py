from math import factorial


class Solution:
    def numTrees(self, n: int) -> int:
        # DP
        # A BST with i nodes can be split into three parts:
        # - Root (1 node)
        # - Left child (j nodes)
        # - Right child (i - 1 - j nodes)
        # G = [0] * (n + 1)
        # G[0] = G[1] = 1
        # for i in range(2, n + 1):
        #     for j in range(i):
        #         G[i] += G[j] * G[i - 1 - j]
        # return G[n]

        # Catalan number
        return factorial(2 * n) // factorial(n) // factorial(n + 1)

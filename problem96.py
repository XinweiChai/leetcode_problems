from math import factorial


class Solution:
    def numTrees(self, n: int) -> int:
        # DP
        # G = [0] * (n + 1)
        # G[0] = G[1] = 1
        # for i in range(2, n + 1):
        #     for j in range(1, i + 1):
        #         G[i] += G[j - 1] * G[i - j]
        # return G[n]

        # Catalan number
        return factorial(2 * n) // factorial(n) // factorial(n + 1)

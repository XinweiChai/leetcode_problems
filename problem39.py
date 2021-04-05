class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # def recursion(state, sum, cur):
        #     if target == sum:
        #         temp = []
        #         for i in range(len(state)):
        #             for j in range(state[i]):
        #                 temp.append(candidates[i])
        #         valid_sum.append(temp)
        #         return
        #     if cur < 0:
        #         return
        #     if target - sum >= candidates[cur]:
        #         state[cur] += 1
        #         recursion(state, sum + candidates[cur], cur)
        #         state[cur] -= 1
        #     recursion(state, sum, cur - 1)

        # def rec2(temp, sum, cur):
        #     if target == sum:
        #         valid_sum.append(temp)
        #         return
        #     if cur < 0:
        #         return
        #     if target - sum >= candidates[cur]:
        #         rec2(temp + [candidates[cur]], sum + candidates[cur], cur)
        #     rec2(temp, sum, cur - 1)
        #
        # valid_sum = []
        # # recursion([0] * len(candidates), 0, len(candidates) - 1)
        # rec2([], 0, len(candidates) - 1)
        # return valid_sum

        # DP
        # candidates.sort()
        # dp = [[[]]] + [[] for _ in range(target)]
        # for i in range(1, target + 1):
        #     for number in candidates:
        #         if number <= i:
        #             for L in dp[i - number]:
        #                 if not L or number >= L[-1]:
        #                     dp[i].append(L + [number])
        # return dp[target]

        # Backtrack
        def bt(cur, cand, tot):
            if not tot:
                res.append(cur)
            for i in range(len(cand)):
                if tot - cand[i] >= 0:
                    bt(cur + [cand[i]], cand[i:], tot - cand[i])

        res = []
        candidates.sort()
        bt([], candidates, target)
        return res


print(Solution().combinationSum([2, 3, 6, 7], 7))

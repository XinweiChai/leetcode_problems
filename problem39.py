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

        def rec2(temp, sum, cur):
            if target == sum:
                valid_sum.append(temp)
                return
            if cur < 0:
                return
            if target - sum >= candidates[cur]:
                rec2(temp + [candidates[cur]], sum + candidates[cur], cur)
            rec2(temp, sum, cur - 1)

        valid_sum = []
        # recursion([0] * len(candidates), 0, len(candidates) - 1)
        rec2([], 0, len(candidates) - 1)
        return valid_sum


print(Solution().combinationSum([2, 3, 6, 7], 7))

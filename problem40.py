from typing import List


class Solution(object):
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # count = {}
        # used = {}
        # for i in candidates:
        #     if i in count.keys():
        #         count[i] += 1
        #     else:
        #         count[i] = 1
        #         used[i] = 0
        # candidates = list(set(candidates))
        #
        # def rec(temp, sum, cur, used):
        #     if target == sum:
        #         valid_sum.append(temp)
        #         return
        #     if cur < 0:
        #         return
        #     if target - sum >= candidates[cur] and used[candidates[cur]] < count[candidates[cur]]:
        #         used[candidates[cur]] += 1
        #         rec(temp + [candidates[cur]], sum + candidates[cur], cur, used)
        #         used[candidates[cur]] -= 1
        #     rec(temp, sum, cur - 1, used)

        candidates.sort(reverse=True)

        def rec2(temp, sum, cur):
            if target == sum:
                valid_sum.append(temp)
                return
            if cur < 0:
                return
            if target - sum >= candidates[cur]:
                rec2(temp + [candidates[cur]], sum + candidates[cur], cur - 1)
            count = 1
            while cur >= count and candidates[cur] == candidates[cur - count]:
                count += 1
            rec2(temp, sum, cur - count)

        valid_sum = []
        # rec([], 0, len(candidates) - 1, used)
        rec2([], 0, len(candidates) - 1)
        return valid_sum


print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))

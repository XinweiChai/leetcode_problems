from typing import Sequence


class Solution:
    def permuteUnique(self, nums: Sequence[int]) -> Sequence[Sequence[int]]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        def perm(cur, available):
            if len(cur) == len(nums):
                res.append(cur)
            else:
                for i in available:
                    if available[i] > 0:
                        available[i] -= 1
                        perm(cur + [i], available)
                        available[i] += 1

        res = []
        perm([], freq)
        return res

        # Via sort
        # nums.sort()
        # res = []
        #
        # def perm(cur, nums):
        #     if not nums:
        #         res.append(cur)
        #         return
        #     for i in range(len(nums)):
        #         if i == len(nums) - 1 or nums[i] != nums[i + 1]:
        #             last = nums[i]
        #             p = i
        #             while p < len(nums) and nums[p] == last:
        #                 perm(cur + [nums[p]] * (p - i + 1), nums[:i] + nums[p + 1:])
        #                 p += 1
        #
        # perm([], nums)
        # return res


print(Solution().permuteUnique([1, 1, 2, 2]))

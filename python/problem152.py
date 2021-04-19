from typing import List


class Solution(object):
    def maxProduct(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return nums[0]
        # left = 0
        # res = -float('inf')
        #
        # def product(start, end):
        #     if start >= end + 1:
        #         return -float('inf')
        #     prod = 1
        #     for i in range(start, end + 1):
        #         prod *= nums[i]
        #     return prod
        #
        # neg = []
        # for i in range(len(nums) + 1):
        #     if i == len(nums) or nums[i] == 0:
        #         if len(neg) % 2 == 0:
        #             res = max(res, product(left, i - 1))
        #         else:
        #             res = max(res, product(left, neg[-1] - 1), product(neg[0] + 1, i - 1))
        #         if i != len(nums):
        #             res = max(res, 0)
        #         neg = []
        #         left = i + 1
        #     elif nums[i] < 0:
        #         neg.append(i)
        # return res

        res = min_val = max_val = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                min_val, max_val = max_val, min_val
            max_val = max(nums[i] * max_val, nums[i])
            min_val = min(nums[i] * min_val, nums[i])
            res = max(res, max_val)
        return res


print(Solution().maxProduct([2,3,-2,4]))

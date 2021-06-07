from typing import List
import math


# class Solution:
#     def maximumGap(self, nums: List[int]) -> int:
#         min_val = min(nums)
#         max_val = max(nums)
#         if len(nums) <= 2:
#             return max_val - min_val
#         if max_val == min_val:
#             return 0
#         gap = math.ceil((max_val - min_val) / (len(nums) - 1))
#         bucket_max = [-1 for _ in range(len(nums) - 1)]
#         bucket_min = [-1 for _ in range(len(nums) - 1)]
#         for i in nums:
#             pos = (i - min_val) // gap
#             if pos == len(nums) - 1:
#                 pos -= 1
#             bucket_max[pos] = i if bucket_max[pos] == -1 else max(bucket_max[pos], i)
#             bucket_min[pos] = i if bucket_min[pos] == -1 else min(bucket_min[pos], i)
#         prev = bucket_max[0]
#         max_diff = 0
#         for i in range(1, len(nums) - 1):
#             if bucket_max[i] == -1:
#                 continue
#             max_diff = max(max_diff, bucket_min[i] - prev)
#             prev = bucket_max[i]
#         return max_diff


class Solution:
    def maximumGap(self, nums):
        lo, hi, n = min(nums), max(nums), len(nums)
        if n <= 2 or hi == lo:
            return hi - lo
        B = {}
        for num in nums:
            ind = n - 2 if num == hi else (num - lo) * (n - 1) // (hi - lo)
            if ind in B:
                B[ind].append(num)
            else:
                B[ind] = [num]
        cands = [[min(B[i]), max(B[i])] for i in range(n - 1) if i in B]
        return max(y[0] - x[1] for x, y in zip(cands, cands[1:]))


if __name__ == '__main__':
    print(Solution().maximumGap([1,2,3,100]))

from typing import List


class Solution(object):
    def jump(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return 0
        # times = [pow(10, 5) + 1] * len(nums)
        # times[-1] = 0
        # for i in range(len(nums) - 2, -1, -1):
        #     temp = times[i + 1:min(len(nums), i + nums[i] + 1)]
        #     if temp:
        #         times[i] = min(temp) + 1
        # return times[0]
        if len(nums) == 1:
            return 0
        steps = 1
        p = 0
        begin = 1
        while nums[p] + p < len(nums) - 1:
            long_dist = 0
            for i in range(begin, nums[p] + p + 1):
                if i + nums[i] >= long_dist:
                    p = i
                    long_dist = i + nums[i]
            begin = i + 1
            steps += 1
        return steps


print(Solution().jump([2, 3, 0, 1, 4]))

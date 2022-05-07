from typing import Sequence


class Solution:
    def minPatches(self, nums: Sequence[int], n: int) -> int:
        max_range = 1
        cnt = 0
        ptr = 0
        while n >= max_range:
            if ptr < len(nums) and nums[ptr] <= max_range:
                max_range += nums[ptr]
                ptr += 1
            else:
                cnt += 1
                max_range *= 2
        return cnt


if __name__ == '__main__':
    print(Solution().minPatches(nums=[1, 5, 10], n=20))

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = len(nums) + 1
        l_ptr = 0
        for r_ptr in range(len(nums)):
            target -= nums[r_ptr]
            while target <= 0:
                min_len = min(min_len, r_ptr - l_ptr + 1)
                target += nums[l_ptr]
                l_ptr += 1
        return min_len % (len(nums) + 1)


if __name__ == '__main__':
    print(Solution().minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))

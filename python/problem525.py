from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        left = {0: -1}
        cur = 0
        max_len = 0
        for idx, i in enumerate(nums):
            cur += (i << 1) - 1
            if cur in left:
                max_len = max(max_len, idx - left[cur])
            else:
                left[cur] = idx
        return max_len


if __name__ == '__main__':
    print(Solution().findMaxLength([0, 1, 0, 1]))

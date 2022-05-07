from typing import Sequence


class Solution:
    def totalHammingDistance(self, nums: Sequence[int]) -> int:
        digits = [0] * 30
        for i in nums:
            pos = 0
            while i:
                digits[pos] += i & 1
                pos += 1
                i >>= 1
        return sum(i * (len(nums) - i) for i in digits)


if __name__ == '__main__':
    print(Solution().totalHammingDistance([4, 14, 2]))

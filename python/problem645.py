from typing import Sequence


class Solution:
    def findErrorNums(self, nums: Sequence[int]) -> Sequence[int]:
        diff = 0
        square_diff = 0
        for idx, i in enumerate(nums):
            diff += (idx + 1) - i
            square_diff += (idx + 1) * (idx + 1) - i * i
        sum = square_diff // diff
        return [(sum - diff) // 2, (sum + diff) // 2]

    def findErrorNums2(self, nums: Sequence[int]) -> Sequence[int]:
        dup = -1
        missing = 1
        for n in nums:
            if nums[abs(n) - 1] < 0:
                dup = abs(n)
            else:
                nums[abs(n) - 1] *= -1
        for i in range(1, len(nums)):
            if nums[i] > 0:
                missing = i + 1
        return [dup, missing]

    def findErrorNums3(self, nums: Sequence[int]) -> Sequence[int]:
        xor = xor0 = xor1 = 0
        for n in nums:
            xor ^= n
        for i in range(1, len(nums) + 1):
            xor ^= i
        rightmostbit = xor & ~(xor - 1)
        for n in nums:
            if (n & rightmostbit) != 0:
                xor1 ^= n
            else:
                xor0 ^= n

        for i in range(1, len(nums) + 1):
            if (i & rightmostbit) != 0:
                xor1 ^= i
            else:
                xor0 ^= i

        for i in nums:
            if i == xor0:
                return [xor0, xor1]
        return [xor1, xor0]


if __name__ == '__main__':
    print(Solution().findErrorNums3([1, 2, 2, 4]))

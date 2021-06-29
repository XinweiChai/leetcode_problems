from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0] * (len(nums) + 1)
        tot = 0
        for i in range(len(nums)):
            tot += nums[i]
            self.sums[i + 1] = tot

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right + 1] - self.sums[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

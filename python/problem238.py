from typing import List


class Solution(object):
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        top = [1] * len(nums)
        # Top triangle
        temp = 1
        for i in range(1, len(nums)):
            temp *= nums[i-1]
            top[i] = temp
        # Bottom triangle
        temp = 1
        for i in range(len(nums)-2,-1,-1):
            temp *= nums[i+1]
            top[i] *= temp
        return top

print(Solution().productExceptSelf([2,3,4,5]))
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        top = [1] * len(nums)
        temp = 1
        for i in range(1, len(nums)):
            temp *= nums[i-1]
            top[i] = temp
        temp = 1
        for i in range(len(nums)-2,-1,-1):
            temp *= nums[i+1]
            top[i] *= temp
        return top
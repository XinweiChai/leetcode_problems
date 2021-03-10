class Solution:
    def missingNumber(self, nums) -> int:
        # return (len(nums)*(len(nums)+1))//2 - sum(nums)
        missing = 0
        for i in nums:
            missing ^= i
        for i in range(len(nums)):
            missing ^= (i + 1)
        return missing


print(Solution().missingNumber([3, 0, 1]))

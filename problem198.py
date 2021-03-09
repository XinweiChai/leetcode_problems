class Solution:
    def rob(self, nums) -> int:
        # My solution
        # if not nums:
        #     return 0
        # elif len(nums) <= 3:
        #     nums += [0, 0]
        #     return max(nums[0] + nums[2], nums[1])
        # nums[2] += nums[0]
        # pos = 3
        # while pos < len(nums):
        #     nums[pos] += max(nums[pos - 2], nums[pos - 3])
        #     pos += 1
        # return max(nums[-1], nums[-2])
        # Clever
        last, now = 0, 0
        for i in nums:
            last, now = now, max(last + i, now)
        return now


print(Solution().rob([1, 3, 1, 3, 100]))

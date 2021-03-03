class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        num = 1
        p = 0
        while p <= len(nums) - 1:
            if nums[p] == num:
                num += 1
            elif nums[p] > num:
                break
            p += 1
        return num


print(Solution().firstMissingPositive([1, 2, 4, 5]))

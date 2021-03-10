class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cur = 1
        while cur < len(nums):
            if nums[cur] == nums[cur-1]:
                nums.pop(cur)
            else:
                cur += 1
        return cur
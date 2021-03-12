class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tortoise = nums[0]
        hare = nums[nums[0]]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
        tortoise = 0
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        return tortoise


print(Solution().findDuplicate([3, 1, 3, 4, 2]))

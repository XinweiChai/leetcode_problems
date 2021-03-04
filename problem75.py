class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Bubble sort
        # for i in range(len(nums) - 1):
        #     for j in range(len(nums)-i-1):
        #         if nums[j] > nums[j + 1]:
        #             nums[j], nums[j + 1] = nums[j + 1], nums[j]
        # return nums

        # Cheat
        # zeros = 0
        # ones = 0
        # twos = 0
        # for i in nums:
        #     if i == 0:
        #         zeros += 1
        #     elif i == 1:
        #         ones += 1
        #     else:
        #         twos += 1
        # for i in range(len(nums)):
        #     if zeros > 0:
        #         nums[i] = 0
        #         zeros -= 1
        #     elif ones > 0:
        #         nums[i] = 1
        #         ones -= 1
        #     elif twos > 0:
        #         nums[i] = 2
        #         twos -= 1
        # return nums

        # Three pointers
        left = 0

        def update(left, num):
            while nums[left] == num and left < len(nums) - 1:
                left += 1
            return left

        left = update(left, 0)
        for i in range(left, len(nums)):
            if nums[i] == 0 and i > left:
                nums[i], nums[left] = nums[left], nums[i]
                left = update(left, 0)

        left = update(left, 1)
        for i in range(left, len(nums)):
            if nums[i] == 1 and i > left:
                nums[i], nums[left] = nums[left], nums[i]
                left = update(left, 1)
        return nums


print(Solution().sortColors([1,2,1]))

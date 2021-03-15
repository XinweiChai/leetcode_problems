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

        # Cheat (two passes)
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

        # Dutch partitioning problem
        red, white, blue = 0, 0, len(nums) - 1

        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1


print(Solution().sortColors([1,2,1]))

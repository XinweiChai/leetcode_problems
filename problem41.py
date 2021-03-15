class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(nlogn)
        # nums.sort()
        # num = 1
        # p = 0
        # while p <= len(nums) - 1:
        #     if nums[p] == num:
        #         num += 1
        #     elif nums[p] > num:
        #         break
        #     p += 1
        # return num

        # O(n)
        nums.append(0)
        n = len(nums)
        for i in range(n):  # delete those useless elements
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        for i in range(n):  # use the index as the hash to record the frequency of each number
            nums[nums[i] % n] += n
        for i in range(1, n):
            if nums[i] < n:
                return i
        return n

        # O(n)
        # A = nums
        # n = len(nums)
        # for i in range(n):
        #     while 0 < A[i] <= n and A[A[i] - 1] != A[i]:
        #         temp = A[A[i] - 1]
        #         A[A[i] - 1] = A[i]
        #         A[i] = temp
        #
        # for i in range(n):
        #     if A[i] != i + 1:
        #         return i + 1
        # return n + 1


print(Solution().firstMissingPositive([3, 4, -1, 1]))

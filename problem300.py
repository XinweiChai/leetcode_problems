class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # DP
        # table = [1]
        # for i in range(1, len(nums)):
        #     max_count = 0
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             max_count = max(max_count, table[j])
        #     table.append(max_count + 1)
        # return max(table)
        dp = [0] * len(nums)

        def binary_search(left, right, num):
            if left == right:
                return left
            mid = (left + right) // 2
            if num <= dp[mid]:
                return binary_search(left, mid, num)
            else:
                return binary_search(mid + 1, right, num)

        l = 0
        for num in nums:
            i = binary_search(0, l, num)
            dp[i] = num
            if i == l:
                l += 1
        return l


print(Solution().lengthOfLIS([3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12]))

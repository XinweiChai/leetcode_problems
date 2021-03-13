class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def binary_search(left, right, num):
            if left == right:
                return left
            mid = (left + right) // 2
            if num <= sorted_list[mid]:
                return binary_search(left, mid, num)
            else:
                return binary_search(mid + 1, right, num)

        res = [0] * len(nums)
        sorted_list = []
        for i in range(len(nums) - 1, -1, -1):
            pos = binary_search(0, len(sorted_list), nums[i])
            sorted_list.insert(pos, nums[i])
            res[i] = pos
        return res


print(Solution().countSmaller([5, 2, 6, 1]))

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # def binary_search(left, right, num):
        #     if left == right:
        #         return left
        #     mid = (left + right) // 2
        #     if num <= sorted_list[mid]:
        #         return binary_search(left, mid, num)
        #     else:
        #         return binary_search(mid + 1, right, num)
        #
        # res = [0] * len(nums)
        # sorted_list = []
        # for i in range(len(nums) - 1, -1, -1):
        #     pos = binary_search(0, len(sorted_list), nums[i])
        #     # Wrong! This step costs O(n)
        #     sorted_list.insert(pos, nums[i])
        #     res[i] = pos
        # return res

        # Count during mergesort
        def sort(enum):
            half = len(enum) // 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum

        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller


print(Solution().countSmaller([5, 2, 6, 1]))

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype -> List[List[int]]
        """
        # Enumeration
        # res = [[]]
        # for i in nums:
        #     for j in range(len(res)):
        #         res.append(res[j]+[i])
        # return res

        # Bitmask
        n = len(nums)
        output = []

        for i in range(2 ** n, 2 ** (n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])

        return output

print(Solution().subsets([1, 2, 3]))

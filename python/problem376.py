from typing import Sequence


class Solution:
    class Solution:
        def wiggleMaxLength(self, nums: Sequence[int]) -> int:
            if len(nums) == 1:
                return 1
            ret = 2

            def comp(x, y):
                if x == y:
                    return 0
                elif x < y:
                    return 1
                else:
                    return -1

            last = comp(nums[0], nums[1])
            if last == 0:
                ret = 1
            for i in range(2, len(nums)):
                cur = comp(nums[i - 1], nums[i])
                if (cur > 0 and last <= 0) or (cur < 0 and last >= 0):
                    ret += 1
                    last = cur
            return ret

if __name__ == '__main__':
    print(Solution().wiggleMaxLength([3,3,3,2,5]))

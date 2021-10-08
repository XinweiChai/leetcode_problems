import bisect
from typing import List


class Solution:
    # O(n^2logn)
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        cnt = 0

        for i in range(n - 2):
            if nums[i] == 0:
                continue
            last = i + 2
            for j in range(i + 1, n - 1):
                last = bisect.bisect_left(nums, nums[i] + nums[j], lo=last)
                cnt += last - j - 1
        return cnt

    # linear search approach, O(n^2)
    def triangleNumber2(self, nums: List[int]) -> int:
        nums.sort()
        res = 0

        for k in reversed(range(2, len(nums))):
            lo = 0
            hi = k - 1
            third = nums[k]
            while lo < hi:
                # perform triangle check on current number
                currVal = nums[lo] + nums[hi]
                if currVal > third:
                    res += hi - lo
                    hi -= 1
                else:
                    lo += 1

        return res

if __name__ == '__main__':
    print(Solution().triangleNumber([7, 0, 0, 0]))

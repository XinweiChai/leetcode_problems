from typing import List


class Solution:
    # TO
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) <= 1:
            return False
        sum_n = sum(nums)
        cur = 0
        while cur <= sum_n:
            tot = nums[0] + nums[1]
            l = 0
            r = 1
            while 1:
                if tot == cur:
                    return True
                if l == r - 1 or tot < cur:
                    r += 1
                    if r == len(nums):
                        break
                    tot += nums[r]
                elif tot > cur:
                    tot -= nums[l]
                    l += 1
            cur += k
        return False

    def checkSubarraySum2(self, nums: List[int], k: int) -> bool:
        preRemainder = {0: -1}

        cur = 0
        for i in range(len(nums)):
            cur += nums[i]

            if cur % k in preRemainder:
                if i - preRemainder[cur % k] > 1:
                    return True
            else:
                preRemainder[cur % k] = i

        return False


if __name__ == '__main__':
    print(Solution().checkSubarraySum2(nums=[1, 2, 12], k=6))

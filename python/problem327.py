from typing import Sequence


class Solution:
    # Naive approach O(n^2)
    # def countRangeSum(self, nums: Sequence[int], lower: int, upper: int) -> int:
    #     cnt = 0
    #     for i in range(len(nums)):
    #         tot = 0
    #         for j in range(i, len(nums)):
    #             tot += nums[j]
    #             if lower <= tot <= upper:
    #                 cnt += 1
    #     return cnt

    # O(nlogn)
    def countRangeSum(self, nums: Sequence[int], lower: int, upper: int) -> int:
        first = [0]
        for num in nums:
            first.append(first[-1] + num)

        def sort(lo, hi):
            mid = (lo + hi) // 2
            if mid == lo:
                return 0
            count = sort(lo, mid) + sort(mid, hi)
            i = j = mid
            for left in first[lo:mid]:
                while i < hi and first[i] - left < lower:
                    i += 1
                while j < hi and first[j] - left <= upper:
                    j += 1
                count += j - i
            first[lo:hi] = sorted(first[lo:hi])
            return count

        return sort(0, len(first))


if __name__ == '__main__':
    print(Solution().countRangeSum(nums=[-2, 5, -1], lower=-2, upper=2))

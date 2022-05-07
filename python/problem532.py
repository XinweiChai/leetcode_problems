from collections import Counter
from typing import Sequence


class Solution:
    def findPairs(self, nums: Sequence[int], k: int) -> int:
        nums = sorted(nums)
        pairs = set()
        l = 0
        r = 0
        while r < len(nums):
            if l >= r or nums[r] - nums[l] < k:
                r += 1
            else:
                if nums[r] - nums[l] == k:
                    pairs.add((nums[l], nums[r]))
                l += 1
        return len(pairs)

    # Clean solution
    def findPairs2(self, nums: Sequence[int], k: int) -> int:
        if k == 0:
            counter = Counter(nums)
            return sum(counter[i] > 1 for i in counter)
        counter = set(nums)
        return sum(i + k in counter for i in counter)


if __name__ == '__main__':
    print(Solution().findPairs(nums=[3, 1, 4, 1, 5], k=2))

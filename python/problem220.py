from typing import Sequence


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: Sequence[int], k: int, t: int) -> bool:
        d = {}
        if t == 0:
            for idx, i in enumerate(nums):
                if i in d and idx - d[i] <= k:
                    return True
                d[i] = idx
            return False
        for idx, i in enumerate(nums):
            if idx > k:
                d.pop(nums[idx - k - 1] // t)
            buck = i // t
            if buck in d or (buck - 1 in d and i - d[buck - 1] <= t) or (buck + 1 in d and d[buck + 1] - i <= t):
                return True
            d[buck] = i
        return False


if __name__ == '__main__':
    print(Solution().containsNearbyAlmostDuplicate(nums=[1, 5, 9, 1, 5, 9], k=2, t=3))

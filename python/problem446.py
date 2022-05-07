from typing import Sequence
from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, nums: Sequence[int]) -> int:
        n = len(nums)
        f = [{} for _ in range(n)]  # map from (i, d) to freq
        cnt = 0
        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                cnt += f[j].get(diff, 0)
                f[i][diff] = f[i].get(diff, 0) + f[j].get(diff, 0) + 1
        return cnt

    def numberOfArithmeticSlices2(self, nums: Sequence[int]) -> int:
        positions = defaultdict(list)
        n = len(nums) - 1
        for i, a in enumerate(reversed(nums)):
            positions[a].append(n - i)
        previous = defaultdict(int)
        subseqs = [defaultdict(int) for _ in range(len(nums))]
        for i, a in enumerate(nums):
            del positions[a][-1]
            if not positions[a]:
                del positions[a]
            if len(positions) > len(previous):
                for b in previous:
                    c = (a << 1) - b
                    if c in positions:
                        n = previous[b] + subseqs[i][b]
                        for j in positions[c]:
                            if j <= i:
                                break
                            subseqs[j][a] += n
            else:
                for c in positions:
                    b = (a << 1) - c
                    if b in previous:
                        n = previous[b] + subseqs[i][b]
                        for j in positions[c]:
                            subseqs[j][a] += n
            previous[a] += 1
        return sum(sum(p.values()) for p in subseqs)


if __name__ == '__main__':
    print(Solution().numberOfArithmeticSlices2([1, 1, 2, 3, 4, 5]))

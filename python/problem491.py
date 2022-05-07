from typing import Sequence


class Solution:
    def findSubsequences(self, nums: Sequence[int]) -> Sequence[Sequence[int]]:
        subs = {()}
        for num in nums:
            subs |= {sub + (num,) for sub in subs if not sub or sub[-1] <= num}
        return [list(sub) for sub in subs if len(sub) >= 2]

    def findSubsequences2(self, nums: Sequence[int]) -> Sequence[Sequence[int]]:
        res = set()

        def dfs(i, path):
            if len(path) > 1:
                res.add(tuple(path[:]))

            for j in range(i, len(nums)):
                if not path or path[-1] <= nums[j]:
                    dfs(j + 1, path + [nums[j]])

        dfs(0, [])
        return list(res)


if __name__ == '__main__':
    print(Solution().findSubsequences2([1, 2, 3, 1, 1, 1, 1]))

from typing import Sequence


class Solution:
    # Time out, even with cumulative sum and max and memoization
    def splitArray(self, nums: Sequence[int], m: int) -> int:
        n = len(nums)
        memo = {}
        cumul_sum = [0] * (n + 1)
        cumul_max = [0] * n
        for i in range(n):
            cumul_sum[i + 1] += cumul_sum[i] + nums[i]
            cumul_max[-i - 1] = max(cumul_max[-i], nums[-i - 1])

        def dfs(pos, split):
            if (pos, split) not in memo:
                if split == 0:
                    # memo[pos, split] = sum(nums[pos:])
                    memo[pos, split] = cumul_sum[n] - cumul_sum[pos]
                elif split == n - pos:
                    # memo[pos, split] = max(nums[pos:])
                    memo[pos, split] = cumul_max[pos]
                else:
                    # memo[pos, split] = min(max(sum(nums[pos:i]), dfs(i, split - 1)) for i in range(pos + 1, n - split + 1))
                    memo[pos, split] = min(max(cumul_sum[i] - cumul_sum[pos], dfs(i, split - 1)) for i in range(pos + 1, n - split + 1))
            return memo[pos, split]

        return dfs(0, m - 1)


    def splitArray2(self, nums: Sequence[int], m: int) -> int:
        low, high, ans = max(nums), sum(nums), -1

        def is_valid(m, mid):
            # assume mid is < max(nums)
            cuts, curr_sum = 0, 0
            for x in nums:
                curr_sum += x
                if curr_sum > mid:
                    cuts, curr_sum = cuts + 1, x
            subs = cuts + 1
            return subs <= m

        while low <= high:
            mid = (low + high) // 2
            if is_valid(m, mid):  # can you make at-most m sub-arrays with maximum sum atmost mid
                ans, high = mid, mid - 1
            else:
                low = mid + 1
        return ans


if __name__ == '__main__':
    # print(Solution().splitArray([10, 5, 13, 4, 8, 4, 5, 11, 14, 9, 16, 10, 20, 8], 8))
    print(Solution().splitArray([7,2,5,10,8], 2))

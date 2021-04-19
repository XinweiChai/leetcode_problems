class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            if 1 & n:
                count += 1
            n = n >> 1
        return count


print(Solution().hammingWeight(5))

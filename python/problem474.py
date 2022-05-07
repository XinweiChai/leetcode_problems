from typing import Sequence


class Solution:
    def findMaxForm(self, strs: Sequence[str], m: int, n: int) -> int:
        strs = sorted((i.count('0'), i.count('1')) for i in strs)

        memo = {}

        def dp(p, zeros, ones):
            if zeros < 0 or ones < 0:
                return -1
            if p == len(strs):
                return 0
            if (p, zeros, ones) not in memo:
                memo[p, zeros, ones] = max(dp(p + 1, zeros - strs[p][0], ones - strs[p][1]) + 1,
                                             dp(p + 1, zeros, ones))
            return memo[p, zeros, ones]

        return dp(0, m, n)

    def findMaxForm2(self, strs: Sequence[str], m: int, n: int) -> int:
        strs = [(i.count('0'), i.count('1')) for i in strs]

        def getResult(s, zero, one):
            result = 0
            for t in s:
                if zero - t[0] >= 0 and one - t[1] >= 0:
                    result += 1
                    zero -= t[0]
                    one -= t[1]
            return result

        # 3 cases
        # Case 1(r1): we sorted zeros
        # Case 2(r2): we sorted ones
        # Case 3(r3): we sorted it by max size of zero+ones
        strs.sort(key=lambda tup: tup[0])
        r1 = getResult(strs, m, n)
        strs.sort(key=lambda tup: tup[1])
        r2 = getResult(strs, m, n)
        strs.sort(key=lambda tup: (tup[0] + tup[1], tup[0]))
        r3 = getResult(strs, m, n)
        return max(r1, r2, r3)


if __name__ == '__main__':
    print(Solution().findMaxForm2(["11111", "100", "1101", "1101", "11000"], 5, 7))

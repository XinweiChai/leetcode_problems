class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        res = {i: 1 for i in p}  # num of strings end with i
        l = 1
        for i, j in zip(p, p[1:]):
            l = l + 1 if (ord(j) - ord(i)) % 26 == 1 else 1
            res[j] = max(res[j], l)
        return sum(res.values())

    def findSubstringInWraproundString2(self, p: str) -> int:
        p = '^' + p
        seen = {}
        for i in range(1, len(p)):
            if ord(p[i]) - ord(p[i - 1]) == 1 or ord(p[i]) - ord(p[i - 1]) == -25:
                prev_len += 1
            else:
                prev_len = 1
            if prev_len > seen.get(p[i], 0):
                seen[p[i]] = prev_len
        return sum(seen.values())


if __name__ == '__main__':
    print(Solution().findSubstringInWraproundString2("zab"))

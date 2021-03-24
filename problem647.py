class Solution:
    def countSubstrings(self, s: str) -> int:
        def palindromes_at_p(p):
            count = 1
            step = 1
            while p - step >= 0 and p + step < len(s) and s[p - step] == s[p + step]:
                count += 1
                step += 1
            step = 0
            while p - step >= 0 and p + step + 1 < len(s) and s[p - step] == s[p + step + 1]:
                count += 1
                step += 1
            return count

        cnt = 0
        for i in range(len(s)):
            cnt += palindromes_at_p(i)
        return cnt


print(Solution().countSubstrings("abc"))

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        cur = ''
        n = len(s)
        for i in range(n):
            cur += s[i]
            if n % (i + 1) == 0 and s.count(cur) == n // (i+1):
                return True
        return False

if __name__ == '__main__':
    print(Solution().repeatedSubstringPattern("aba"))
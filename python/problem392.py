class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start_s = start_t = 0
        while 1:
            if start_s == len(s):
                return True
            if start_t == len(t):
                return False
            if s[start_s] == t[start_t]:
                start_s += 1
            start_t += 1


if __name__ == '__main__':
    print(Solution().isSubsequence("abc", "ahbgdc"))

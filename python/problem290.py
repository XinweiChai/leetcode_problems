class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        d2 = {}
        s = s.split(' ')
        if len(pattern) != len(s):
            return False
        for idx, i in enumerate(pattern):
            if i not in d and s[idx] not in d2:
                d[i] = s[idx]
                d2[s[idx]] = i
            elif i not in d or s[idx] not in d2 or d[i] != s[idx] or d2[s[idx]] != i:
                return False
        return True


if __name__ == '__main__':
    print(Solution().wordPattern(pattern="abc", s="dog cat dog"))

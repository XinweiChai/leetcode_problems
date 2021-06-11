class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1 = {}
        d2 = set()
        for i in range(len(s)):
            if s[i] in d1:
                if d1[s[i]] != t[i]:
                    return False
            else:
                if t[i] in d2:
                    return False
                d1[s[i]] = t[i]
                d2.add(t[i])
        return True


if __name__ == '__main__':
    print(Solution().isIsomorphic(s="paper", t="title"))

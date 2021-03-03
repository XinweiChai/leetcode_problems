class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s
        first_match = bool(s) and p[0] in ['?', s[0]]
        if p[0] == '*':
            if len(p) > 1 and p[1] == '*':
                return self.isMatch(s, p[1:])
            if s:
                return self.isMatch(s, p[1:]) or self.isMatch(s[1:], p)
            else:
                return self.isMatch(s, p[1:])
        else:
            return first_match and self.isMatch(s[1:], p[1:])


print(Solution().isMatch("babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb",
"b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"))

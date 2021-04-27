from collections import Counter


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) <= 1:
            return s1 == s2
        l = len(s1)
        ct1 = Counter()
        ct2 = Counter()
        ct2_rev = Counter()
        for i in range(1, l):
            ct1.update(s1[i - 1])
            ct2.update(s2[i - 1])
            ct2_rev.update(s2[-i])
            # if Counter(s1[:i]) == Counter(s2[:i]) and self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
            if ct1 == ct2 and self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            # elif Counter(s1[:i]) == Counter(s2[l-i:]) and self.isScramble(s1[:i], s2[l - i:]) and self.isScramble(s1[i:], s2[:l - i]):
            elif ct1 == ct2_rev and self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False


print(Solution().isScramble('abb', 'bab'))
print(Solution().isScramble('abcde', 'caebd'))
print(Solution().isScramble('great', 'aterg'))

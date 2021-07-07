class Solution:
    def removeDuplicateLetters(self, s):
        for c in sorted(set(s)):
            suffix = s[s.index(c):]
            if set(suffix) == set(s):
                return c + self.removeDuplicateLetters(suffix.replace(c, ''))
        return ''

    def removeDuplicateLetters2(self, s):
        rindex = {c: i for i, c in enumerate(s)}
        result = ''
        res_set = set()
        for i, c in enumerate(s):
            if c not in res_set:
                while c < result[-1:] and i < rindex[result[-1]]:
                    res_set.discard(result[-1:])
                    result = result[:-1]
                result += c
                res_set.add(c)
        return result

if __name__ == '__main__':
    print(Solution().removeDuplicateLetters2("cbacdcbc"))

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
        for i, c in enumerate(s):
            if c not in result:
                while c < result[-1:] and i < rindex[result[-1]]:
                    result = result[:-1]
                result += c
        return result

if __name__ == '__main__':
    print(Solution().removeDuplicateLetters2("cbacdcbc"))

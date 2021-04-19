class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        common = ""
        pos = 0
        while 1:
            if pos >= len(strs[0]):
                return common
            to_compare = strs[0][pos]
            for i in strs:
                if pos >= len(i) or to_compare != i[pos]:
                    return common
            pos += 1
            common += to_compare


print(Solution().longestCommonPrefix(['']))

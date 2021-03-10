class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            left = 0
            cur = i
            flag = True
            while left < len(needle):
                if haystack[cur] == needle[left]:
                    cur += 1
                    left += 1
                else:
                    flag = False
                    break
            if flag:
                return i
        return -1

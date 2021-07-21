class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

    def strStr2(self, haystack: str, needle: str) -> int:
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

    # Using KMP algorithm
    def strStr3(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        if not n:
            return 0

        def kmpTable():
            table = [0] * n
            table[0] = -1
            pos = 1
            cnd = 0
            while pos < n:
                if needle[pos] == needle[cnd]:
                    table[pos] = table[cnd]
                else:
                    table[pos] = cnd
                    while cnd >= 0 and needle[pos] != needle[cnd]:
                        cnd = table[cnd]
                pos += 1
                cnd += 1
            return table

        T = kmpTable()
        i = j = 0
        while i < m:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == n:
                    return i - j
            else:
                j = T[j]
                if j < 0:
                    i += 1
                    j += 1
        return -1


if __name__ == '__main__':
    print(Solution().strStr3(haystack="aabaaabaaac", needle="aabaaac"))

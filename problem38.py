class Solution(object):
    def countAndSay(self, n: int) -> str:
        s = "1"
        for i in range(n - 1):
            p = 0
            temp = ""
            count = 1
            while p <= len(s) - 1:
                if p != len(s) - 1 and s[p] == s[p + 1]:
                    count += 1
                else:
                    temp += str(count) + s[p]
                    count = 1
                p += 1
            s = temp
        return s


print(Solution().countAndSay(3))

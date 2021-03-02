class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        p = 0
        res = 0
        while p < len(s) and s[p] == ' ':
            p += 1
        sign = 1
        if p < len(s) and s[p] == '+':
            p += 1
        elif p < len(s) and s[p] == '-':
            p += 1
            sign = -1
        while p < len(s) and s[p] == '0':
            p += 1
        num = ''
        while p < len(s) and '0' <= s[p] <= '9':
            num += s[p]
            p += 1
        if num:
            res = res + int(num) * sign
        if res > pow(2, 31) - 1:
            res = 2147483647
        elif res < -pow(2, 31):
            res = -2147483648
        return res


print(Solution().myAtoi('+10'))

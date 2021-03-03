class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        def to_num(c):
            return ord(c) - ord('0')

        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i + j] += to_num(num1[len(num1) - 1 - i]) * to_num(num2[len(num2) - 1 - j])
                res[i + j + 1] += res[i + j] // 10
                res[i + j] -= (res[i + j] // 10) * 10
        s = ''
        while res and res[-1] == 0:
            res = res[:-1]
        if not res:
            return '0'
        for i in range(len(res) - 1, -1, -1):
            s += str(res[i])
        return s


print(Solution().multiply('0', '0'))

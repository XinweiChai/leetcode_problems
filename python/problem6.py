class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype -> str
        """
        if numRows == 1:
            return s
        period = 2 * numRows - 2
        temp = ''
        for i in range(numRows):
            for j in range(len(s) // period + 1):
                if j * period + i < len(s):
                    temp += s[j * period + i]
                if 0 < i < numRows - 1 and (j + 1) * period - i < len(s):
                    temp += s[(j + 1) * period - i]
        return temp


print(Solution().convert('PAYPALISHIRING', 2))

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # title = ""
        # while columnNumber!=0:
        #     res=columnNumber%26
        #     if res == 0:
        #         res = 26
        #         columnNumber -= 26
        #     title = chr(res + ord('A') - 1) + title
        #     columnNumber//=26
        # return title

        # One-line solution
        return "" if columnNumber == 0 else self.convertToTitle((columnNumber - 1) // 26) + chr(
            (columnNumber - 1) % 26 + ord('A'))


if __name__ == '__main__':
    print(Solution().convertToTitle(5))

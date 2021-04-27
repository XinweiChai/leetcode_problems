from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1], [1, 1]]
        for i in range(2, numRows):
            temp = [1] * (i + 1)
            for j in range(1, i):
                temp[j] = ans[i - 1][j] + ans[i - 1][j - 1]
            ans.append(temp)
        return ans[:numRows]

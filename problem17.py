from typing import List


class Solution(object):
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = [""]
        char_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        for i in digits:
            res_len = len(res)
            for k in range(1, len(char_dict[i])):
                for j in range(res_len):
                    res.append(res[j] + char_dict[i][k])
            for j in range(res_len):
                res[j] += char_dict[i][0]
        return res


print(Solution().letterCombinations("23"))

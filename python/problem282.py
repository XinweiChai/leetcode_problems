from typing import List
from itertools import product
import re


class Solution:

    # Too slow
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        for i in product(['+', '-', '*', ''], repeat=len(num) - 1):
            expr = ''.join([num[j] + i[j] for j in range(len(num) - 1)] + [num[-1]])
            if not re.search(r'(^|\D)0+\d', expr) and eval(expr) == target:
                res.append(expr)
        return res

    # A little bit faster
    def addOperators2(self, num: str, target: int) -> List[str]:
        res = []

        def dfs(done, todo, last_num):
            if todo < len(num):
                if last_num:
                    dfs(done + num[todo], todo + 1, True)
                dfs(done + '+' + num[todo], todo + 1, num[todo] != '0')
                dfs(done + '-' + num[todo], todo + 1, num[todo] != '0')
                dfs(done + '*' + num[todo], todo + 1, num[todo] != '0')
            else:
                if eval(done) == target:
                    res.append(done)

        dfs(num[0], 1, num[0] != '0')
        return res

    # Another version of solution 2
    def addOperators3(self, num: str, target: int) -> List[str]:
        res = []

        def dfs(done, todo):
            if todo < len(num):
                for i in range(todo + 1, (todo + 1 if num[todo] == '0' else len(num)) + 1):
                    dfs(done + '+' + num[todo:i], i)
                    dfs(done + '-' + num[todo:i], i)
                    dfs(done + '*' + num[todo:i], i)
            else:
                if eval(done) == target:
                    res.append(done)

        for i in range(1, (1 if num[0] == '0' else len(num)) + 1):
            dfs(num[:i], i)
        return res

    # eval(done) in solution 2 and solution 3 repeatedly computes the result of prefix,
    # thus this solution is much faster
    def addOperators4(self, num: str, target: int) -> List[str]:
        res = []

        def dfs(num, temp, cur, last):
            if not num:
                if cur == target:
                    res.append(temp)
                return
            for i in range(1, 2 if num[0] == '0' else len(num) + 1):
                val = num[:i]
                dfs(num[i:], temp + "+" + val, cur + int(val), int(val))
                dfs(num[i:], temp + "-" + val, cur - int(val), -int(val))
                dfs(num[i:], temp + "*" + val, cur - last + last * int(val), last * int(val))

        for i in range(1, 2 if num[0] == '0' else len(num) + 1):
            dfs(num[i:], num[:i], int(num[:i]), int(num[:i]))
        return res

    # Optimize string-copy
    def addOperators5(self, num: str, target: int) -> List[str]:
        res = []

        def dfs(start, temp, cur, last):
            if start == len(num):
                if cur == target:
                    res.append(temp)
                return
            for i in range(start + 1, start + 2 if num[start] == '0' else len(num) + 1):
                val = num[start:i]
                dfs(i, temp + "+" + val, cur + int(val), int(val))
                dfs(i, temp + "-" + val, cur - int(val), -int(val))
                dfs(i, temp + "*" + val, cur - last + last * int(val), last * int(val))

        for i in range(1, 2 if num[0] == '0' else len(num) + 1):
            dfs(i, num[:i], int(num[:i]), int(num[:i]))
        return res


if __name__ == '__main__':
    print(Solution().addOperators5(num="10009", target=9))

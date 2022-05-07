from typing import Sequence


class Solution:
    def diffWaysToCompute(self, expression: str) -> Sequence[int]:
        memo = {}

        def compute(x, y, operator):
            d = {'+': x + y, '-': x - y, '*': x * y}
            return d[operator]

        def dfs(start, end):
            if (start, end) not in memo:
                if expression[start:end].isdigit():
                    memo[start, end] = [int(expression[start:end])]
                else:
                    memo[start, end] = []
                    for i in range(start, end):
                        if expression[i] in '+-*':
                            left = dfs(start, i)
                            right = dfs(i + 1, end)
                            memo[start, end].extend(compute(x, y, expression[i]) for x in left for y in right)
            return memo[start, end]

        return dfs(0, len(expression))


if __name__ == '__main__':
    print(Solution().diffWaysToCompute("22*3-4*5"))

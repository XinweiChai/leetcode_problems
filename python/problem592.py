class Solution:
    def fractionAddition(self, expression: str) -> str:
        import math
        from collections import deque

        if expression[0] != '+' and expression[0] != '-':
            expression = '+' + expression

        n = len(expression)
        indexes = []
        exp = deque([])
        fractions = deque([])
        for idx, v in enumerate(expression):
            if v == '+' or v == '-':
                indexes.append(idx)
                exp.append(v)
        indexes.append(n)

        for j in range(len(indexes) - 1):
            fraction = expression[indexes[j] + 1:indexes[j + 1]]

            s = fraction.split('/')
            a, b = int(s[0]), int(s[1])
            fractions.append((a, b))

        res = [0, 1]  # a, b
        assert len(exp) == len(fractions)

        while fractions:
            sign = exp.popleft()
            x, y = fractions.popleft()
            if sign == '+':
                res[0] = res[0] * y + res[1] * x
            else:
                res[0] = res[0] * y - res[1] * x
            res[1] = res[1] * y

        if res[0] == 0:
            return "0/1"
        d = math.gcd(res[0], res[1])
        res[0] = res[0] // d
        res[1] = res[1] // d
        return str(res[0]) + "/" + str(res[1])

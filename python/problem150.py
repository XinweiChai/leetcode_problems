from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if '0' <= i[0] <= '9' or (i[0] == '-' and len(i) > 1):
                stack.append(int(i))
            else:
                one, two = stack.pop(), stack.pop()
                if i == '+':
                    stack.append(two + one)
                elif i == '-':
                    stack.append(two - one)
                elif i == '*':
                    stack.append(two * one)
                elif i == '/':
                    # stack.append(two // one)
                    if two == 0:
                        stack.append(0)
                    else:
                        stack.append(two // abs(two) * one // abs(one) * (abs(two) // abs(one)))
        return stack[0]


# print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
print(Solution().evalRPN(['0', '3', '/']))

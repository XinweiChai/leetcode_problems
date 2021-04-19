import re


class Solution(object):
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        nums = re.split('[+\-*/]', s)
        nums = [int(i) for i in nums]
        operators = re.split('\d+', s)[1:-1]
        p = 0
        while p < len(operators):
            if operators[p] == '*':
                nums[p] *= nums[p + 1]
                nums.pop(p + 1)
                operators.pop(p)
            elif operators[p] == '/':
                nums[p] //= nums[p + 1]
                nums.pop(p + 1)
                operators.pop(p)
            else:
                p += 1
        while operators:
            if operators[0] == '+':
                nums[0] += nums[1]
                nums.pop(1)
            elif operators[0] == '-':
                nums[0] -= nums[1]
                nums.pop(1)
            operators.pop(0)
        return nums[0]


print(Solution().calculate(" 12 - 5/2"))

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        exp = []
        res = 0
        cur_num = 0
        for i in s:
            if i.isdigit():
            elif i == '(':
            elif i == ')':
            elif i == '+':
            elif i == '-':

if __name__ == '__main__':
    print(Solution().calculate("1+1"))
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k and stack and stack[-1] > digit:
                k -= 1
                stack.pop()
            stack.append(digit)
        if k:
            stack = stack[:-k]
        return "".join(stack).lstrip("0") or "0"


if __name__ == '__main__':
    print(Solution().removeKdigits(num="1234567890", k=9))

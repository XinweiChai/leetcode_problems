class Solution:
    def calculate(self, s: str) -> int:
        stack = [[]]
        cur_num = 0
        ptr = stack[-1]

        def ev(expr):
            sgn = 1
            res = 0
            for i in expr:
                if i == '-':
                    sgn *= -1
                else:
                    res += i * sgn
                    sgn = 1
            return res

        for i in s:
            if i.isdigit():
                if i == '0' and not cur_num:
                    ptr.append(0)
                else:
                    cur_num = 10 * cur_num + int(i)
            else:
                if cur_num:
                    ptr.append(cur_num)
                    cur_num = 0
                if i == '(':
                    ptr.append([])
                    stack.append(ptr[-1])
                    ptr = stack[-1]
                elif i == ')':
                    stack[-1][-1] = ev(stack.pop())
                    ptr = stack[-1]
                elif i == '-':
                    ptr.append(i)
        if cur_num:
            ptr.append(cur_num)
        return ev(stack[-1])

    def calculate2(self, s: str) -> int:

        stack = []
        operand = 0
        res = 0  # For the on-going result
        sign = 1  # 1 means positive, -1 means negative

        for ch in s:
            if ch.isdigit():

                # Forming operand, since it could be more than one digit
                operand = (operand * 10) + int(ch)

            elif ch == '+':

                # Evaluate the expression to the left,
                # with result, sign, operand
                res += sign * operand

                # Save the recently encountered '+' sign
                sign = 1

                # Reset operand
                operand = 0

            elif ch == '-':

                res += sign * operand
                sign = -1
                operand = 0

            elif ch == '(':

                # Push the result and sign on to the stack, for later
                # We push the result first, then sign
                stack.append(res)
                stack.append(sign)

                # Reset operand and result, as if new evaluation begins for the new sub-expression
                sign = 1
                res = 0

            elif ch == ')':

                # Evaluate the expression to the left
                # with result, sign and operand
                res += sign * operand

                # ')' marks end of expression within a set of parenthesis
                # Its result is multiplied with sign on top of stack
                # as stack.pop() is the sign before the parenthesis
                res *= stack.pop()  # stack pop 1, sign

                # Then add to the next operand on the top.
                # as stack.pop() is the result calculated before this parenthesis
                # (operand on stack) + (sign on stack * (result from parenthesis))
                res += stack.pop()  # stack pop 2, operand

                # Reset the operand
                operand = 0

        return res + sign * operand


if __name__ == '__main__':
    print(Solution().calculate2("(1+3)-(2+4)"))

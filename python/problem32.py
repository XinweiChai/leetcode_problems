class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Using 2 stacks
        # if not s:
        #     return 0
        # stack = []
        # idx_stack = [-1]
        # for i in range(len(s)):
        #     if s[i] == ')' and stack and stack[-1] == '(':
        #         stack.pop()
        #         idx_stack.pop()
        #     else:
        #         stack.append(s[i])
        #         idx_stack.append(i)
        # idx_stack.append(len(s))
        # return max([idx_stack[i] - idx_stack[i - 1] - 1 for i in range(1, len(idx_stack))])

        # Using 1 stack
        stack = [-1]
        max_par = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_par = max(max_par, i - stack[-1])
        return max_par


print(Solution().longestValidParentheses(")(()((())"))

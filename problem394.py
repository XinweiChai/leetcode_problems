import re


class Solution:
    def decodeString(self, s):
        # Using stack
        stack = []
        cnt = 0
        cur = ''
        for i in s:
            if i.isdigit():
                cnt = cnt * 10 + int(i)
            elif i == '[':
                stack.append(cur)
                cur = ''
                stack.append(cnt)
                cnt = 0
            elif i == ']':
                prev = stack.pop() * cur
                cur = stack.pop() + prev
            else:
                cur += i
        return cur
#
#         # Using regex
#         while '[' in s:
#             s = re.sub(r'(\d+)\[([a-z]*)\]', lambda m: int(m.group(1)) * m.group(2), s)
#         return s




# print(Solution().decodeString("a2[c]bb"))
print(Solution().decodeString("3[a2[c]]3[a]"))

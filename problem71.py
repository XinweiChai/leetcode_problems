import re


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = re.split("/+", path.strip('/'))
        for i in paths:
            if i == '..':
                stack.pop()
            elif i == '.':
                pass
            else:
                stack.append(i)
        return '/' + '/'.join(stack)


print(Solution().simplifyPath("/home//foo/"))

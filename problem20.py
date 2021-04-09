class Solution(object):
    def isValid(self, s: str) -> bool:
        par_list = []
        for i in s:
            if i in ['(', '[', '{']:
                par_list.append(i)
            elif not par_list:
                return False
            else:
                if (i == ')' and par_list[-1] == '(') or (i == ']' and par_list[-1] == '[') or (i == '}' and par_list[-1] == '{'):
                    par_list.pop()
                else:
                    return False
        return not par_list


print(Solution().isValid("()[]{}"))

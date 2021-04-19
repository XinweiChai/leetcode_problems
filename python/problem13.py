class Solution(object):
    def romanToInt(self, s: str) -> int:
        symb_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        sum = 0
        p = 0
        while p < len(s):
            if p < len(s) - 1 and symb_dict[s[p]] < symb_dict[s[p + 1]]:
                sum -= symb_dict[s[p]]
            else:
                sum += symb_dict[s[p]]
            p += 1
        return sum


print(Solution().romanToInt("IV"))

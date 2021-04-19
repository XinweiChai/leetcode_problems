class Solution:
    def isNumber(self, s: str) -> bool:
        DFA = {0: {'sign': 1, 'dot': 2, 'digit': 3},
               1: {'dot': 2, 'digit': 3},
               2: {'digit': 4},
               3: {'digit': 3, 'dot': 4, 'e': 5},
               4: {'digit': 4, 'e': 5},
               5: {'sign': 6, 'digit': 7},
               6: {'digit': 7},
               7: {'digit': 7}}
        cur = 0
        for i in s:
            if i.isdigit():
                act = 'digit'
            elif i == '+' or i == '-':
                act = 'sign'
            elif i == '.':
                act = 'dot'
            elif i == 'e' or i == 'E':
                act = 'e'
            else:
                return False
            if act not in DFA[cur]:
                return False
            cur = DFA[cur][act]
        if cur in {3, 4, 7}:
            return True
        return False


print(Solution().isNumber("2e0"))

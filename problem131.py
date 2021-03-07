class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s) - 1
        table = [[False] * (len(s)) for _ in range(len(s))]
        for i in range(len(s)):
            table[i][i] = True
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                table[i][i + 1] = True
        for i in range(len(s)):
            step = 0
            while 0 <= i - step - 1 and i + step + 1 <= len(s) - 1 and s[i - step - 1] == s[i + step + 1] and \
                    table[i - step][i + step]:
                table[i - step - 1][i + step + 1] = True
                step += 1
            step = 0
            while 0 <= i - step - 1 and i + step + 2 <= len(s) - 1 and s[i - step - 1] == s[i + step + 2] and \
                    table[i - step][i + step + 1]:
                table[i - step - 1][i + step + 2] = True
                step += 1

        def is_palindrome(s):
            if len(s) <= 1:
                return True
            if s[0] != s[-1]:
                return False
            return is_palindrome(s[1:-1])

        sets = []
        for i in range(2 ** n, 2 ** (n + 1)):
            bars = bin(i)[3:]
            ind = [i for i in range(len(bars)) if bars[i] == '1'] + [len(s)-1]
            temp = []
            cur = 0
            flag = True
            for i in ind:
                if not table[cur][i]:
                    flag = False
                    break
                cur = i + 1
            if flag:
                cur = 0
                for i in ind:
                    temp.append(s[cur:i + 1])
                    cur = i + 1
                sets.append(temp)

            # for i in ind:
            #     temp.append(s[cur:i + 1])
            #     cur = i + 1
            # flag = True
            # for i in temp:
            #     if not is_palindrome(i):
            #     flag = False
            #     break
            # if flag:
            #     sets.append(temp)
        return sets


print(Solution().partition("abbab"))

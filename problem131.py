class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        table = [[False] * (len(s)) for _ in range(len(s))]
        for i in range(len(s)):
            table[i][i] = True
        for i in range(len(s)):
            step = 0
            while 0 <= i - step - 1 and i + step + 1 <= len(s) - 1 and s[i - step - 1] == s[i + step + 1] and \
                    table[i - step][i + step]:
                table[i - step - 1][i + step + 1] = True
                step += 1
            step = 0
            while 0 <= i - step and i + step + 1 <= len(s) - 1 and s[i - step] == s[i + step + 1]:
                if step == 0 or table[i - step + 1][i + step]:
                    table[i - step][i + step + 1] = True
                    step += 1

        sets = []

        def dfs(left, cur_list):
            if left == len(s):
                sets.append(cur_list)
            for i in range(left, len(s)):
                if table[left][i]:
                    dfs(i + 1, cur_list + [s[left:i + 1]])

        dfs(0, [])
        return sets

        # Stupid enumeration
        # for i in range(2 ** n, 2 ** (n + 1)):
        #     bars = bin(i)[3:]
        #     ind = [i for i in range(len(bars)) if bars[i] == '1'] + [len(s) - 1]
        #     temp = []
        #     cur = 0
        #     flag = True
        #     for i in ind:
        #         if not table[cur][i]:
        #             flag = False
        #             break
        #         cur = i + 1
        #     if flag:
        #         cur = 0
        #         for i in ind:
        #             temp.append(s[cur:i + 1])
        #             cur = i + 1
        #         sets.append(temp)
        #
        # return sets


print(Solution().partition("abbab"))

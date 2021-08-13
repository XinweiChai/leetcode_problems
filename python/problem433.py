from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def valid_mutation(x, y):
            one = True
            for i, j in zip(x, y):
                if i != j:
                    if one:
                        one = False
                    else:
                        return False
            return True

        cnt = 1
        curr = [start]
        while 1:
            if not curr:
                return -1
            temp = []
            for i in curr:
                j = len(bank) - 1
                while j >= 0:
                    jth = bank[j]
                    if valid_mutation(i, jth):
                        if jth == end:
                            return cnt
                        else:
                            temp.append(jth)
                            bank.pop(j)
                    j -= 1
            curr = temp
            cnt += 1


if __name__ == '__main__':
    print(Solution().minMutation("AACCTTGG", "AATTCCGG", ["AATTCCGG", "AACCTGGG", "AACCCCGG", "AACCTACC"]))

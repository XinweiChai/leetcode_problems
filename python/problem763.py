from typing import List
from collections import Counter


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # c1 = Counter(S)
        # c2 = Counter()
        # to_satisfy = 0
        # satisfied = 0
        # ans = []
        # last = -1
        # for i in range(len(S)):
        #     if S[i] not in c2:
        #         to_satisfy += 1
        #     c2[S[i]] += 1
        #     if c2[S[i]] == c1[S[i]]:
        #         satisfied += 1
        #     if satisfied == to_satisfy:
        #         ans.append(i - last)
        #         last = i
        # return ans

        # A more concise one
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1

        return ans
print(Solution().partitionLabels("ababcbacadefegdehijhklij"))

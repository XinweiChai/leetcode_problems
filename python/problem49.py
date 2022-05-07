from typing import Sequence


class Solution:
    def groupAnagrams(self, strs: Sequence[str]) -> Sequence[Sequence[str]]:
        ans = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            if tuple(count) in ans.keys():
                ans[tuple(count)].append(s)
            else:
                ans[tuple(count)] = [s]
        return ans.values()


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # In tutorial
        # unique_char = set()
        # for i in s:
        #     if len(unique_char) == 26:
        #         break
        #     unique_char.add(i)
        # res = 0
        # for i in range(1, 1 + len(unique_char)):
        #     l = r = 0
        #     c = Counter()
        #     count_at_least_k = 0
        #     while r < len(s):
        #         if len(c) > i:
        #             if c[s[l]] == k:
        #                 count_at_least_k -= 1
        #             c[s[l]] -= 1
        #             if c[s[l]] ==0:
        #                 c.pop(s[l])
        #             l += 1
        #         else:
        #             c[s[r]] += 1
        #             if c[s[r]] == k:
        #                 count_at_least_k += 1
        #             r += 1
        #         if len(c) == i and len(c) == count_at_least_k:
        #             res = max(r - l, res)
        # return res

        # Recurrent
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)

print(Solution().longestSubstring('aaabb', 3))

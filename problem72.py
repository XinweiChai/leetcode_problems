class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return max(len(word1), len(word2))
        cur1 = 0
        cur2 = 0
        min_dist = 0
        l = 0
        r = 1
        while r <= len(word1):
            p = word2[cur2:].find(word1[l])
            if p != -1:
                while word2[cur2:].find(word1[l:r]) != -1 and r <= len(word1):
                    r += 1
                r -= 1
                # p += cur2
                if abs(l - cur1 - p) <= (r - l):
                    min_dist += max(l - cur1, p)
                    cur1 = r
                    cur2 += p + r - l
                # else:
                #     r = l + 1
            l = r
            r += 1
        min_dist += max(len(word1) - cur1, len(word2) - cur2)
        return min_dist


print(Solution().minDistance("abcde", "xyaef"))
print(Solution().minDistance("aeea", "ebeb"))
print(Solution().minDistance("intention", "execution"))
print(Solution().minDistance("plasma", "altruism"))

import bisect
from collections import defaultdict
from functools import cache


class Solution:
    # find() takes too much time
    @cache
    def minDistance(self, word1: str, word2: str) -> int:
        last_pos = len(word2)
        if not word1:
            return len(word2)
        min_dist = float('inf')
        used = set()
        for i in range(len(word1)):
            if word1[i] in used:
                continue
            used.add(word1[i])
            pos = word2.find(word1[i])
            if pos == -1:
                min_dist = min(min_dist, self.minDistance(word1[i + 1:], word2) + i + 1)
            else:
                if pos < last_pos:
                    last_pos = pos
                    min_dist = min(min_dist, self.minDistance(word1[i + 1:], word2[pos + 1:]) + i + pos)
        return min_dist

    # A better solution
    def minDistance2(self, word1: str, word2: str) -> int:
        letter_dict = defaultdict(list)
        for i, c in enumerate(word2):
            letter_dict[c].append(i)
        dp = [0] * (len(word2) + 1)

        for i in range(len(word1) - 1, -1, -1):
            last_match = 0
            for match_in_word2 in letter_dict[word1[i]]:
                for j in range(last_match, match_in_word2 + 1):
                    dp[j] = max(1 + dp[match_in_word2 + 1], dp[j])
                last_match = match_in_word2 + 1

        return len(word1) + len(word2) - 2 * dp[0]

    # Insane
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)

        charPos1 = defaultdict(list)
        charPos2 = defaultdict(list)
        for i, c in enumerate(text1):
            charPos1[c].append(i)

        for i, c in enumerate(text2):
            charPos2[c].append(i)

        text1 += "$"
        heap = []
        for i in range(n - 1, -1, -1):
            for idx in charPos2[text1[i]]:
                j = bisect.bisect_right(heap, idx)
                if j == 0:
                    heap.insert(0, idx)
                else:
                    heap[j - 1] = idx

        return len(heap)

if __name__ == '__main__':
    print(Solution().minDistance2("bbba", "abbb"))

from collections import deque


class Solution:
    # My solution
    def characterReplacement(self, s: str, k: int) -> int:
        def index(x):
            return ord(x) - ord('A')

        n = len(s)
        rest = [k] * 26
        pos = [deque() for _ in range(26)]
        max_streak = 0
        for idx, i in enumerate(s):
            if pos[index(i)]:
                rest[index(i)] -= idx - pos[index(i)][-1] - 1
            pos[index(i)].append(idx)
            while rest[index(i)] < 0:
                rest[index(i)] -= pos[index(i)].popleft() - pos[index(i)][0] + 1
            max_streak = max(max_streak, len(pos[index(i)]) + k - rest[index(i)] + min(rest[index(i)],
                                                                                       n - pos[index(i)][-1] - 1 +
                                                                                       pos[index(i)][0]))

        return max_streak

    # Smarter solution, using sliding window
    def characterReplacement2(self, s: str, k: int) -> int:
        max_freq = res = 0
        count = {}
        for idx, i in enumerate(s):
            count[i] = count.get(i, 0) + 1
            max_freq = max(max_freq, count[i])
            if res - max_freq < k:
                res += 1
            else:
                count[s[idx - res]] -= 1
        return res


if __name__ == '__main__':
    # print(Solution().characterReplacement(s="AABABBA", k=2))
    print(Solution().characterReplacement2(s="ABAB", k=2))

import collections


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # d = {}
        # a = 0
        # b = 0
        # bs = {}
        # for idx, i in enumerate(secret):
        #     if i in d:
        #         d[i][0].append(idx)
        #         d[i][1] += 1
        #     else:
        #         d[i] = [[idx], 1]
        # for idx, i in enumerate(guess):
        #     if i in d:
        #         if idx in d[i][0]:
        #             a += 1
        #             d[i][1] -= 1
        #         else:
        #             bs[i] = bs[i] + 1 if i in bs else 1
        #         if d[i][1] == 0:
        #             d.pop(i)
        # for i in bs:
        #     if i in d:
        #         b += min(d[i][1], bs[i])
        # return f"{a}A{b}B"

        # A short one
        A = sum(a == b for a, b in zip(secret, guess))
        B = collections.Counter(secret) & collections.Counter(guess)
        return "%dA%dB" % (A, sum(B.values()) - A)


if __name__ == '__main__':
    print(Solution().getHint("1122", "1222"))

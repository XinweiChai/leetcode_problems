from itertools import groupby


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        n = len(hand)
        board = [''.join(g) for _, g in groupby(board)]
        hand = {i: hand.count(i) for i in set(hand)}

        def update(b, p):
            b.pop(p)
            if p != 0 and p != len(b):
                if b[p - 1][0] == b[p][0]:
                    b[p - 1] += b[p]
                    b.pop(p)
                    if len(b[p - 1]) >= 3:
                        return update(b, p - 1)
            return b

        def rec(b, h):
            if not b:
                return sum(h.values())
            if not h:
                return -1
            ptr = 0
            res = -1
            while ptr < len(b):
                cur = b[ptr]
                c = cur[0]
                if cur.count(c) + h.get(c, 0) >= 3:
                    h[c] -= 3 - cur.count(c)
                    if h[c] == 0:
                        h.pop(c)
                    temp = update(b.copy(), ptr)
                    res = max(res, rec(temp, h))
                    h[c] = h.get(c, 0) + 3 - cur.count(c)
                ptr += 1
            return res

        temp = rec(board, hand)
        if temp == -1:
            return temp
        return n - temp


if __name__ == '__main__':
    print(Solution().findMinStep(board="RRWWRRBBRR", hand="WB"))

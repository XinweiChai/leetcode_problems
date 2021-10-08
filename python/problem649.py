from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rs, ds = deque(), deque()
        for idx, i in enumerate(senate):
            if i == 'R':
                rs.appendleft(idx)
            else:
                ds.appendleft(idx)

        cur = -1
        while rs and ds:
            if rs[-1] > cur and (ds[-1] <= cur or ds[-1] > rs[-1]):
                cur = rs[-1]
                ds.pop()
                rs.appendleft(rs.pop())
            elif ds[-1] > cur and (rs[-1] <= cur or rs[-1] > ds[-1]):
                cur = ds[-1]
                rs.pop()
                ds.appendleft(ds.pop())
            else:
                cur = -1
        if rs:
            return "Radiant"
        return "Dire"

    # A more clever solution
    def predictPartyVictory2(self, senate):
        n = len(senate)
        R, D = deque(), deque()
        for i in range(n):
            if senate[i] == "D":
                D.append(i)
            else:
                R.append(i)

        while D and R:
            if D[0] > R[0]:
                R.append(R[0] + n)
            else:
                D.append(D[0] + n)

            D.popleft()
            R.popleft()

        return "Dire" if D else "Radiant"


if __name__ == '__main__':
    print(Solution().predictPartyVictory("DDRRR"))

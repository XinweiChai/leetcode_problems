from typing import Sequence


class Solution:
    def validSquare(self, p1: Sequence[int], p2: Sequence[int], p3: Sequence[int], p4: Sequence[int]) -> bool:
        cnt = 0
        p1 = tuple(p1)
        p2 = tuple(p2)
        p3 = tuple(p3)
        p4 = tuple(p4)
        pts = {p1, p2, p3, p4}
        if len(pts) != 4:
            return False
        for i in p1, p2, p3:
            temp = pts - {i}
            for j in temp:
                r1, r2 = temp - {j}
                if (r1[0] - i[0]) * (r2[0] - i[0]) + (r1[1] - i[1]) * (r2[1] - i[1]) == 0:
                    if (r1[0] - i[0]) ** 2 + (r1[1] - i[1]) ** 2 != (r2[0] - i[0]) ** 2 + (r2[1] - i[1]) ** 2:
                        return False
                    cnt += 1
                    break
        return cnt == 3

    def validSquare2(self, p1: Sequence[int], p2: Sequence[int], p3: Sequence[int], p4: Sequence[int]) -> bool:
        # p1, p2, p3, p4

        # p2p1 needs to be perpendicular to p3p1
        def slope(q1, q2, q3, q4):
            # returns the slope between q1, q2
            k = (q1[1] - q2[1], q1[0] - q2[0])
            l = (q3[1] - q4[1], q3[0] - q4[0])

            sk = k[0] / k[1] if k[1] != 0 else float('inf')
            sl = l[0] / l[1] if l[1] != 0 else float('inf')

            if ({sk, sl} == {0, float('inf')}):
                return True
            elif (sk, sl) == (float('inf'), float('inf')):
                return False
            else:
                # print (k[0]*l[1], -k[1]*l[0])
                return k[0] * l[0] == -k[1] * l[1]

        def dist(q1, q2):
            return (q1[0] - q2[0]) ** 2 + (q1[1] - q2[1]) ** 2

        # p1 p2 p3 p4
        # L(p1p2) perpendicular to L(p1p3)
        # L(p4p2) perpendiculat to L(p4p3)
        # dist(p1p2), dist(p1p3), dist(p4p2), dist(p4p3)
        for x, y, z in [(p1, p2, p3), (p1, p3, p2), (p2, p3, p1)]:
            # check the slope of L(p4x) and L(p4y) to see if they are pependicular
            # check the slope of L(zx) and L(zy) to see if they are pependicular
            # check the distance of L(p4x) and L(p4y) and L(zx) and L(zy) to see if they are all equal

            perpendicularLines = slope(p4, x, p4, y) and slope(z, x, z, y)

            d_p4x = dist(p4, x)
            d_p4y = dist(p4, y)
            d_zx = dist(z, x)
            d_zy = dist(z, y)

            distanceEqual = (d_p4x == d_p4y == d_zx == d_zy)

            if perpendicularLines and distanceEqual:
                return True

        return False


if __name__ == '__main__':
    print(Solution().validSquare([0, 0], [-1, 0], [1, 0], [0, 1]))

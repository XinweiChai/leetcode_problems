class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        tot = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)
        width = max(min(ax2, bx2) - max(ax1, bx1), 0)
        height = max(min(ay2, by2) - max(ay1, by1), 0)
        return tot - width * height


if __name__ == '__main__':
    print(Solution().computeArea(ax1=-3, ay1=0, ax2=3, ay2=4, bx1=0, by1=-1, bx2=9, by2=2))

class Solution:
    def reverse(self, x: int) -> int:
        s = (x > 0) - (x < 0)
        r = int(str(x * s)[::-1])
        return s * r * (r < 2 ** 31)

class Solution(object):
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 <= x < (mid + 1) ** 2:
                return mid
            elif mid ** 2 < x:
                left = mid
            else:
                right = mid

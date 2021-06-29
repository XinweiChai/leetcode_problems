class Solution:
    def arrangeCoins(self, n: int) -> int:
        # left = 1
        # right = int(2 * n ** 0.5)
        # while left <= right:
        #     mid = (left + right) // 2
        #     if mid * (mid + 1) > n * 2:
        #         right = mid - 1
        #     elif (mid + 1) * mid < n * 2:
        #         left = mid + 1
        #     else:
        #         return mid
        # return right

        return int((2 * n + 0.25) ** 0.5 - 0.5)

if __name__ == '__main__':
    print(Solution().arrangeCoins(5))

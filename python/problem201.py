class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        return self.rangeBitwiseAnd(left >> 1, right >> 1) << 1 if left < right else right

    def rangeBitwiseAnd2(self, left: int, right: int) -> int:
        move_factor = 0
        while left != right:
            left >>= 1
            right >>= 1
            move_factor += 1
        return left << move_factor


if __name__ == '__main__':
    print(Solution().rangeBitwiseAnd(4, 5))

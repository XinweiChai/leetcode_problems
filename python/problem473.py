from typing import List


class Solution:
    # Using backtrack
    def makesquare(self, M: List[int]) -> bool:
        M.sort(reverse=True)
        n, side = len(M), sum(M) // 4
        if sum(M) % 4 != 0 or M[0] > side:
            return False

        def btrack(ptr, rest, done):
            if done == 3:
                return True
            if ptr == n:
                return False
            num = M[ptr]
            if num > rest:
                return btrack(ptr + 1, rest, done)
            M[ptr] = side + 1
            if num == rest:
                return btrack(1, side, done + 1)
            else:
                # Use the current match or not
                if btrack(ptr + 1, rest - num, done):
                    return True
                M[ptr] = num
                return btrack(ptr + 1, rest, done)

        return btrack(0, side, 0)


if __name__ == '__main__':
    # print(Solution().makesquare([1, 1, 2, 2, 2]))
    # print(Solution().makesquare([3, 3, 3, 3, 4]))
    print(Solution().makesquare([12, 13, 1, 15, 11, 17, 16, 3, 15, 11, 13, 4, 2, 16, 15]))

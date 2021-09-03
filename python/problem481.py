class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 3:
            return 1
        n -= 3
        ptr = 2
        s = [1, 2, 2]
        while n > 0:
            s.extend([3 - s[-1]] * s[ptr])
            n -= s[ptr]
            ptr += 1
        if n != 0:
            s.pop()
        return s.count(1)


if __name__ == '__main__':
    print(Solution().magicalString(8))

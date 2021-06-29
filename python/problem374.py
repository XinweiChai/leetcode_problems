class Solution:

    def guessNumber(self, n: int) -> int:
        def guess(num, target=6):
            if num == target:
                return 0
            elif num > target:
                return -1
            else:
                return 1

        step = (n + 1) // 2
        num = n // 2
        while 1:
            res = guess(num)
            if res == 0:
                return num
            step = (step + 1) // 2
            num += res * step

if __name__ == '__main__':
    print(Solution().guessNumber(10))

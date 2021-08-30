class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        pivots = {}
        ptr1 = ptr2 = 0
        cnt1 = cnt2 = 0
        last = 0
        while 1:
            if ptr2 == len(s2):
                cnt2 += 1
                ptr2 = 0
            try:
                ptr1 = s1.index(s2[ptr2], ptr1)
                if ptr2 == 0:
                    if ptr1 in pivots:
                        break
                    else:
                        last = cnt2
                        pivots[ptr1] = (cnt1, cnt2)
                ptr1 += 1
                ptr2 += 1
            except ValueError:
                if ptr1 == 0:
                    return 0
                cnt1 += 1
                if cnt1 > n1:
                    return last // n2
                ptr1 = 0
        last1, last2 = pivots[ptr1]
        # flag is for the cases when a pattern does not begin at the beginning of s1
        flag = ptr1 != 0
        repeat, rest = divmod(n1 - last1 - flag, cnt1 - last1)
        return (last2 + repeat * (cnt2 - last2) + self.residual(s1, rest + flag, s2, ptr1)) // n2

    def residual(self, s1: str, n1: int, s2: str, pivot):
        ptr1 = pivot + 1
        ptr2 = 1
        cnt2 = 0
        while n1:
            if ptr2 == len(s2):
                cnt2 += 1
                ptr2 = 0
            try:
                ptr1 = s1.index(s2[ptr2], ptr1) + 1
            except ValueError:
                ptr1 = 0
                n1 -= 1
            ptr2 += 1
        return cnt2


if __name__ == '__main__':
    print(Solution().getMaxRepetitions(s1="baba", n1=11, s2="baab", n2=1))
    print(Solution().getMaxRepetitions("lovelivenanjomusicforever", 100000, "nanjo", 10))
    print(Solution().getMaxRepetitions("aaa", 3, "aa", 1))
    print(Solution().getMaxRepetitions("bacaba", 3, "abacab", 1))

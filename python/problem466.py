class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        try:
            pivot = s1.index(s2[0])
        except ValueError:
            return 0
        ptr1 = pivot + 1
        ptr2 = 1
        cnt1 = 1
        cnt2 = 1
        while ptr1 != len(s1) or ptr2 != len(s2):
            if ptr2 == len(s2):
                cnt2 += 1
                ptr2 = 0
            if ptr1 == len(s1):
                ptr1 = 0
                cnt1 += 1
            try:
                ptr1 = s1.index(s2[ptr2], ptr1) + 1
                ptr2 += 1
            except ValueError:
                if not cnt1:
                    return 0
                ptr1 = len(s1)
                if ptr2 == 0:
                    break
        return n1 // cnt1 * cnt2 // n2 + self.residual(s1, n1 % cnt1, s2, n2)

    def residual(self, s1: str, n1: int, s2: str, n2: int):
        pivot = s1.index(s2[0])
        ptr1 = pivot + 1
        ptr2 = 1
        cnt2 = 0
        while ptr1 != len(s1):
            if ptr2 == len(s2):
                cnt2 += 1
                ptr2 = 0
            try:
                ptr1 = s1.index(s2[ptr2], ptr1) + 1
            except ValueError:
                ptr1 = len(s1)
            ptr2 += 1
        return cnt2


if __name__ == '__main__':
    print(Solution().getMaxRepetitions(s1="baba", n1=11, s2="baab", n2=1))

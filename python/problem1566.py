from typing import Sequence


class Solution:
    def containsPattern(self, arr: Sequence[int], m: int, k: int) -> bool:
        for i in range(len(arr) - m * k + 1):
            flag = True
            pat = arr[i:i + m]
            for j in range(1, k):
                if pat != arr[i + m * j:i + m * (j + 1)]:
                    flag = False
                    break
            if flag:
                return True
        return False

    def containsPattern2(self, arr: list[int], m: int, k: int) -> bool:
        return any(arr[i:i + m] * k == arr[i:i + m * k] for i in range(len(arr) - m * k))


if __name__ == '__main__':
    print(Solution().containsPattern([2, 2], 1, 2))

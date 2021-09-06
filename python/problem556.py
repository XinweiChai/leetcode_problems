import heapq


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        i = len(digits) - 1

        # Find the first digit to be swapped (i - 1), where the digits after it are sorted desc
        while i - 1 >= 0 and digits[i] <= digits[i - 1]:
            i -= 1

        if i == 0:
            return -1

        # Find the digit as small as possible to be swapped with (i - 1)
        j = i
        while j + 1 < len(digits) and digits[j + 1] > digits[i - 1]:
            j += 1

        digits[i - 1], digits[j] = digits[j], digits[i - 1]
        # The rest are sorted desc, reverse to make the whole number the smallest candidate
        digits[i:] = digits[i:][::-1]
        ret = int(''.join(digits))

        return ret if ret < 1 << 31 else -1


if __name__ == '__main__':
    print(Solution().nextGreaterElement(230241))

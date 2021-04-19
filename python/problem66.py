from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        cur = len(digits) - 1
        while digits[cur] == 10 and cur > 0:
            digits[cur] -= 10
            digits[cur - 1] += 1
            cur -= 1
        if digits[0] == 10:
            digits[0] = 0
            return [1] + digits
        else:
            return digits

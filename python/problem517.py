from typing import List


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total, n = sum(machines), len(machines)
        if total % n:
            return -1
        target, res, to_right = total // n, 0, 0
        for m in machines:
            to_right += m - target
            res = max(res, abs(to_right), m - target)
        return res

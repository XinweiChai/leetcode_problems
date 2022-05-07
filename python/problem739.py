from typing import Sequence


class Solution:
    def dailyTemperatures(self, T: Sequence[int]) -> Sequence[int]:
        stack = [(float('inf'), -1)]
        out = [0] * len(T)
        for i in range(len(T)):
            while T[i] > stack[-1][0]:
                x = stack.pop()
                out[x[1]] = i - x[1]
            stack.append((T[i], i))
        return out


print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))

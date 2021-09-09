from functools import lru_cache
from itertools import groupby
from typing import List


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        counter = [[boxes[0], 1]]
        for i in range(1, len(boxes)):
            if boxes[i] == boxes[i - 1]:
                counter[-1][1] += 1
            else:
                counter.append([boxes[i], 1])
        n = len(counter)

        @lru_cache(maxsize=None)
        def dp(lo, hi):
            if lo > hi:
                return 0
            if lo == hi:
                return counter[lo][1] ** 2
            cnt = counter[hi][1]
            temp = 0
            last = hi
            max_val = dp(lo, hi - 1) + cnt ** 2
            for i in range(hi - 1, lo - 1, -1):
                if counter[i][0] == counter[hi][0]:
                    cnt += counter[i][1]
                    temp += dp(i + 1, last - 1)
                    last = i
                    max_val = max(max_val, temp + cnt ** 2 + dp(lo, i - 1))
            return max_val

        return dp(0, n - 1)

    def removeBoxes2(self, boxes: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, j, k):
            if i > j: return 0
            cnt = 0
            while (i + cnt) <= j and boxes[i] == boxes[i + cnt]:
                cnt += 1
            i2 = i + cnt
            res = dfs(i2, j, 0) + (k + cnt) ** 2
            for m in range(i2, j + 1):
                if boxes[m] == boxes[i]:
                    res = max(res, dfs(i2, m - 1, 0) + dfs(m, j, k + cnt))
            return res

        return dfs(0, len(boxes) - 1, 0)

    def removeBoxes3(self, boxes: List[int]) -> int:
        @lru_cache(None)
        def bestScore(boxes, similarCnt):
            color = boxes[0][0]
            if len(boxes) > 1 and boxes[-1][0] == color:
                similarCnt += boxes[0][1] + boxes[-1][1]
                boxes = boxes[1:-1]
            else:
                # Or at least from the left
                similarCnt += boxes[0][1]
                boxes = boxes[1:]
            score = similarCnt ** 2
            if boxes:  # Oh there are more boxes left, have to focus on them first
                # Start assuming there are no same-color boxes left
                score += bestScore(boxes, 0)
                # Then verify by looking for the same colored boxes
                # Sure first and last groups of the rest are different color
                for mid in range(1, len(boxes) - 1):
                    if boxes[mid][0] == color:
                        # Check if removing boxes to the left first improves the score
                        joinedScore = bestScore(boxes[:mid], 0) + bestScore(boxes[mid:], similarCnt)
                        score = max(score, joinedScore)
            return score

        boxGroup = tuple((color, len(list(group))) for color, group in groupby(boxes))
        return bestScore(boxGroup, 0)


if __name__ == '__main__':
    print(Solution().removeBoxes3([1, 2, 2, 2, 1, 2, 1]))

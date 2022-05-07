from functools import lru_cache
from itertools import groupby
from typing import Sequence


class Solution:
    # With no aggregation
    def removeBoxes(self, boxes: Sequence[int]) -> int:
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

    # Better than memorizing the indexes as there are possibly repeated patterns
    def removeBoxes2(self, boxes: Sequence[int]) -> int:
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
    print(Solution().removeBoxes2([5, 3, 10, 5, 3, 3, 3, 5, 10]))

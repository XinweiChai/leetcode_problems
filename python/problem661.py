from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        r = len(img)
        c = len(img[0])

        def neighbor(x, y):
            ret = []
            for dx in [-1, 0, 1]:
                if 0 <= x + dx < r:
                    for dy in [-1, 0, 1]:
                        if 0 <= y + dy < c:
                            ret.append((x + dx, y + dy))
            return ret

        new_image = [[0] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                neighbors = neighbor(i, j)
                new_image[i][j] = int(sum(img[x][y] for x, y in neighbors) / len(neighbors))
        return new_image

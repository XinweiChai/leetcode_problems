from typing import Sequence
import heapq


class Solution:
    def trapRainWater(self, heightMap: Sequence[Sequence[int]]) -> int:
        r = len(heightMap)
        c = len(heightMap[0])
        if r < 3 or c < 3:
            return 0
        visited = [[False] * c for _ in range(r)]
        hp = []
        for i in range(c):
            hp.append((heightMap[0][i], 0, i))
            visited[0][i] = True
            hp.append((heightMap[r - 1][i], r - 1, i))
            visited[r - 1][i] = True
        for i in range(1, r - 1):
            hp.append((heightMap[i][0], i, 0))
            visited[i][0] = True
            hp.append((heightMap[i][c - 1], i, c - 1))
            visited[i][c - 1] = True

        heapq.heapify(hp)
        neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        max_height = 0
        water = 0
        while hp:
            height, x, y = heapq.heappop(hp)
            max_height = max(max_height, height)
            for dx, dy in neighbors:
                if 0 <= x + dx < r and 0 < y + dy < c and not visited[x + dx][y + dy]:
                    if heightMap[x + dx][y + dy] < max_height:
                        water += max_height - heightMap[x + dx][y + dy]
                    heapq.heappush(hp, (heightMap[x + dx][y + dy], x + dx, y + dy))
                    visited[x + dx][y + dy] = True
        return water

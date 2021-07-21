from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        n = len(equations)
        for i in range(n):
            l, r = equations[i]
            graph[l].append((r, values[i]))
            graph[r].append((l, 1 / values[i]))

        def query(l, r):
            if r not in graph:
                return -1.0
            if l == r:
                return 1.0
            visited = set()
            stack = [(l, 1)]
            while stack:
                cur, val = stack.pop()
                visited.add(cur)
                for succ, rate in graph[cur]:
                    if succ not in visited:
                        if succ == r:
                            return val * rate
                        stack.append((succ, val * rate))
            return -1.0

        return [query(l, r) for l, r in queries]

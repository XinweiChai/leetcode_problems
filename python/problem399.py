from collections import defaultdict
from typing import Sequence


class Solution:
    def calcEquation(self, equations: Sequence[Sequence[str]], values: Sequence[float], queries: Sequence[Sequence[str]]) -> Sequence[float]:
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

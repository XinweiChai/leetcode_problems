from typing import Sequence
import collections


class Solution:
    def findItinerary(self, tickets: Sequence[Sequence[str]]) -> Sequence[str]:
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            targets[a].append(b)
        route, stack = [], ['JFK']
        while stack:
            while targets[stack[-1]]:
                stack.append(targets[stack[-1]].pop())
            route.append(stack.pop())
        return route[::-1]


if __name__ == '__main__':
    print(Solution().findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))

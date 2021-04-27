from heapq import heappush, heappop, heapify


class Solution:
    def getSkyline(self, buildings):
        # add start-building events
        # also add end-building events(acts as buildings with 0 height)
        # and sort the events in left -> right order
        events = [(L, -H, R) for L, R, H in buildings]
        events += list({(R, 0, None) for _, R, _ in buildings})
        events.sort()

        # res: result, [x, height]
        # live: heap, [-height, ending position]
        res = [[0, 0]]
        live = [(0, float("inf"))]
        for pos, negH, R in events:
            # 1, pop buildings that are already ended
            # 2, if it's the start-building event, make the building alive
            # 3, if previous keypoint height != current highest height, edit the result
            while live[0][1] <= pos:
                heappop(live)
            if negH:
                heappush(live, (negH, R))
            if res[-1][1] != -live[0][0]:
                res += [[pos, -live[0][0]]]
        return res[1:]

        # actions = []
        # points = []
        # cur = 0
        # rest = [(0, -1)]
        # visited = {-1: 0}
        # for i, b in enumerate(buildings):
        #     actions.append((b[0], -b[2], i))
        #     actions.append((b[1], 0, i))
        # actions.sort()
        #
        # for i in actions:
        #     p, h, idx = i
        #     if h != 0:
        #         heappush(rest, (h, idx))
        #         visited[idx] = h
        #         if h < cur:
        #             cur = h
        #             points.append([p, -cur])
        #     else:
        #         if idx == rest[0][1]:
        #             heappop(rest)
        #             while rest[0][1] not in visited:
        #                 heappop(rest)
        #             if cur != rest[0][0]:
        #                 cur = rest[0][0]
        #                 points.append([p, -cur])
        #         visited.pop(idx)
        # return points


# print(Solution().getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
# print(Solution().getSkyline([[0, 2, 3], [2, 5, 3]]))
print(Solution().getSkyline([[4,9,10],[4,9,15],[4,9,12],[10,12,10],[10,12,8]]))

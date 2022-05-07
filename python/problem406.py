from typing import Sequence


# class Solution:
#     def reconstructQueue(self, people: Sequence[Sequence[int]]) -> Sequence[Sequence[int]]:
#         # Using insert, O(n^2)
#         people.sort(key=lambda x: (-x[0], x[1]))
#         res = []
#         for i in people:
#             res.insert(i[1], i)
#         return res

# O(nlogn) solution
class TreeNode:
    def __init__(self, lo, hi):
        self.val = 1
        self.left = None
        self.right = None
        self.lo = lo
        self.hi = hi


class SegmentTree:
    def __init__(self, N):
        self.root = self.build(0, N - 1)

    def build(self, lo, hi):
        if lo == hi:
            return TreeNode(lo, hi)

        mid = (lo + hi) // 2

        node = TreeNode(lo, hi)

        node.left = self.build(lo, mid)
        node.right = self.build(mid + 1, hi)

        node.val = node.left.val + node.right.val

        return node

    def query(self, node, slot):
        if node.lo == node.hi:
            node.val = 0
            return node.lo

        if node.left.val >= slot:
            ret = self.query(node.left, slot)
        else:
            ret = self.query(node.right, slot - node.left.val)

        node.val = node.left.val + node.right.val

        return ret


class Solution:
    def reconstructQueue(self, people: Sequence[Sequence[int]]) -> Sequence[Sequence[int]]:
        if not people:
            return []
        people.sort(key=lambda x: [x[0], -x[1]])
        N = len(people)
        tree = SegmentTree(N)
        root = tree.root

        ans = [[]] * N

        for h, k in people:
            idx = tree.query(root, k + 1)
            ans[idx] = [h, k]

        return ans


print(Solution().reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))

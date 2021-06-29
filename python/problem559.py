"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import deque


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # Recursive
        # if not root:
        #     return 0
        # return 1 + max([self.maxDepth(i) for i in root.children] + [0])
        # Iterative
        if not root:
            return 0
        q = deque()
        q.append(root)
        depth = 0
        while q:
            size = len(q)
            for i in range(size):
                q.extend(q.popleft().children)
            depth += 1
        return depth

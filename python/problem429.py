"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List
from collections import deque


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        res = []
        stack = deque([root])
        while stack:
            cur = len(stack)
            temp = []
            while cur:
                cur -= 1
                node = stack.popleft()
                temp.append(node.val)
                for children in node.children:
                    if children:
                        stack.append(children)
            res.append(temp)
        return res

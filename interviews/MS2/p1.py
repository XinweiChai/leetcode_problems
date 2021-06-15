"""
Given a list of strings, show the frequency of a given substring
"""
from typing import List


class WordTree:
    def __init__(self, cnt=0):
        self.children = {}
        self.cnt = cnt

    def add_child(self, c):
        if c in self.children:
            self.children[c].cnt += 1
        else:
            self.children[c] = WordTree(1)


def make_tree(ls: List[str]):
    wt = WordTree()
    for i in ls:
        cur = wt
        for j in i:
            cur.add_child(j)
            cur = cur.children[j]
    return wt


def count_sub(sub, wt):
    cnt = 0

    def rec(root, ptr):
        nonlocal cnt
        if ptr == len(sub) - 1:
            cnt += root.cnt
            return
        for i in root.children:
            if sub[ptr] == i:
                rec(root.children[i], ptr + 1)
            else:
                rec(root.children[i], ptr)

    rec(wt, 0)
    return cnt


if __name__ == '__main__':
    t = make_tree(['abc', 'bca', 'acb', 'dc'])
    print(count_sub('bc', t))

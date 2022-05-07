from typing import Sequence, Type, Any
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'val: {self.val}, l_val: {self.left.val if self.left else None}, r_val: {self.right.val if self.right else None}'

    def print_all(self):
        ans = []
        cur = [self]
        flag = True
        while flag:
            flag = False
            temp = []
            res = []
            for i in cur:
                if i:
                    res.append(i.val)
                    if i.left:
                        flag = True
                        temp.append(i.left)
                    else:
                        temp.append(None)
                    if i.right:
                        flag = True
                        temp.append(i.right)
                    else:
                        temp.append(None)
                else:
                    res.append(None)
                    temp.append(None)
                    temp.append(None)
            cur = temp
            ans.append(res)
        temp = ans

        ans = [[str(j) if j is not None else ' ' for j in i] for i in ans]
        for i in range(len(ans) - 2, -1, -1):
            for j in range(len(ans[i])):
                left = ' ' * (len(ans[i + 1][j * 2]) - len(ans[i][j]))
                right = ' ' * (len(ans[i + 1][j * 2 + 1]) - len(ans[i][j]))
                ans[i][j] = left + ans[i][j] + right

        for i in range(len(ans) - 1):
            for j in range(len(ans[i])):
                left = ' ' * (2 ** (len(ans) - 1 - i) - 1)
                right = (2 ** (len(ans) - 1 - i) - 1)
                ans[i][j] = left + ans[i][j] + ' ' * right

        for i in ans:
            print(' '.join(i))
        return temp


def create_tree(l: Sequence[Any], cl: Type = TreeNode):
    assert issubclass(cl, TreeNode)
    if isinstance(l[0], list):
        root = cl(l[0][0])
        cur = [root]
        for i in l[1:]:
            cnt = 0
            temp = []
            for j in cur:
                if j is None:
                    cnt += 2
                    temp.append(None)
                    temp.append(None)
                    continue
                if i[cnt] is not None:
                    j.left = cl(i[cnt])
                temp.append(j.left)
                cnt += 1
                if i[cnt]:
                    j.right = cl(i[cnt])
                temp.append(j.right)
                cnt += 1
            cur = temp
        return root
    else:
        root = TreeNode(l[0])
        q = deque([root])
        for i in range(1, len(l), 2):
            cur = q.popleft()
            if l[i] is not None:
                cur.left = TreeNode(l[i])
                q.append(cur.left)
            if i+1 < len(l) and l[i + 1] is not None:
                cur.right = TreeNode(l[i + 1])
                q.append(cur.right)
        return root


if __name__ == '__main__':
    # x = create_tree([[1], [2, 3], [4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14, 15]])
    x = create_tree([1, 2, 3, 4, None, 6, 7, 8, 9, 12, 13, 14, 15])
    x.print_all()

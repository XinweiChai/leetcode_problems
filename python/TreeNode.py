from typing import List, Type


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}, l: {self.left.val if self.left else None}, r: {self.right.val if self.right else None}'

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


def create_tree(l: List[List], cl: Type = TreeNode):
    assert issubclass(cl, TreeNode)
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





if __name__ == '__main__':
    x = create_tree([[1], [2, 3], [4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14, 15]])
    x.print_all()

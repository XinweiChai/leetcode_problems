from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
        print(ans)
        width = 2 * len(ans[-1]) - 1
        to_print = [' ' * width for _ in range(2 * len(ans) - 1)]


def create_tree(l: List[List]):
    root = TreeNode(l[0][0])
    cur = [root]
    for i in l[1:]:
        cnt = 0
        temp = []
        for j in cur:
            if not j:
                cnt += 2
                temp.append(None)
                temp.append(None)
                continue
            if i[cnt]:
                j.left = TreeNode(i[cnt])
            temp.append(j.left)
            cnt += 1
            if i[cnt]:
                j.right = TreeNode(i[cnt])
            temp.append(j.right)
            cnt += 1
        cur = temp
    return root

from typing import List, Type


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


def create_tree(cl: Type, l: List[List]):
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


def morris_traversal(root: TreeNode) -> None:
    while root:
        if not root.left:
            print(root.val)
            root = root.right
        else:
            pred = root.left
            while pred.right and pred.right != root:
                pred = pred.right
            if not pred.right:
                # print(root.val)  # Preorder
                pred.right = root
                root = root.left
            else:
                print(root.val)  # Inorder
                pred.right = None
                root = root.right


if __name__ == '__main__':
    x = create_tree(TreeNode, [[1], [2, 3], [4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14, 15]])
    x.print_all()
    morris_traversal(x)

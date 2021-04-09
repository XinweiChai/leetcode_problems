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

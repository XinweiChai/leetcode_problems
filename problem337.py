from TreeNode import TreeNode


class Solution:
    def rob(self, root: TreeNode) -> int:
        def rec(node):
            if not node:
                return 0, 0
            l, lc = self.rob(node.left)
            r, rc = self.rob(node.right)
            return max(l + r, node.val + lc + rc), l + r

        return rec(root)[0]

        # DP
        # if not root:
        #     return 0
        #
        # # reform tree into array-based tree
        # tree = []
        # graph = {-1: []}
        # index = -1
        # q = [(root, -1)]
        # while q:
        #     node, parent_index = q.pop(0)
        #     if node:
        #         index += 1
        #         tree.append(node.val)
        #         graph[index] = []
        #         graph[parent_index].append(index)
        #         q.append((node.left, index))
        #         q.append((node.right, index))
        #
        # # represent the maximum start by node i with robbing i
        # dp_rob = [0] * (index + 1)
        #
        # # represent the maximum start by node i without robbing i
        # dp_not_rob = [0] * (index + 1)
        #
        # for i in reversed(range(index + 1)):
        #     if not graph[i]:  # if is leaf
        #         dp_rob[i] = tree[i]
        #         dp_not_rob[i] = 0
        #     else:
        #         dp_rob[i] = tree[i] + sum(dp_not_rob[child]
        #                                   for child in graph[i])
        #         dp_not_rob[i] = sum(max(dp_rob[child], dp_not_rob[child])
        #                             for child in graph[i])
        #
        # return max(dp_rob[0], dp_not_rob[0])

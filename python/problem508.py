from typing import List, Optional

from TreeNode import create_tree, TreeNode


class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        freq = {}

        def analysis(node):
            if not node:
                return 0
            tot = analysis(node.left) + analysis(node.right) + node.val
            freq[tot] = freq.get(tot, 0) + 1
            return tot

        analysis(root)
        max_freq = max(freq.values())
        return [i for i in freq if freq[i] == max_freq]


if __name__ == '__main__':
    print(Solution().findFrequentTreeSum(create_tree([5, 2, -3])))

#include <iostream>
#include <vector>

#include "TreeNode.h"
using namespace std;

class Solution {
   public:
    int sumNumbers(TreeNode *root) {
        int sum = 0;
        rec(root, 0, &sum);
        return sum;
    }

    void rec(TreeNode *node, int cur, int *sum) {
        cur += node->val;
        if (!node->left and !node->right) {
            *sum += cur;
        } else {
            if (node->left) {
                rec(node->left, cur * 10, sum);
            }
            if (node->right) {
                rec(node->right, cur * 10, sum);
            }
        }
    }
};

int main(int argc, char const *argv[]) {
    TreeNode d = TreeNode(5);
    TreeNode e = TreeNode(1);
    TreeNode b = TreeNode(9, &d, &e);
    TreeNode c = TreeNode(0);
    TreeNode a = TreeNode(4, &b, &c);
    cout << Solution().sumNumbers(&a) << endl;
    return 0;
}

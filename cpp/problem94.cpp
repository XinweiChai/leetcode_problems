#include "TreeNode.h"
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        rec(root, res);
        return res;
    }
    void rec(TreeNode* node, vector<int> &res){
        if (node){
            rec(node->left, res);
            res.push_back(node->val);
            rec(node->right,res);
        }
    }
};